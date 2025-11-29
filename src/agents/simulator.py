from typing import List, Dict, Any
import numpy as np
import pandas as pd
import random
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

from src.utils.text_features import count_exclamations, contains_urgency_words, contains_discount


class Simulator:
    def __init__(self, cfg: Dict[str, Any]):
        self.cfg = cfg
        sim_cfg = cfg.get("simulator", {})
        self.min_train = sim_cfg.get("min_train_samples", 40)
        self.seed = sim_cfg.get("random_seed", 42)
        self.tfidf_max = sim_cfg.get("tfidf_max_features", 2000)
        self.model = None
        self.vectorizer = None
        self.vectorizer_fitted = False
        self.feature_names = {}
        random.seed(self.seed)
        np.random.seed(self.seed)

    def _clean(self, s: str) -> str:
        if s is None:
            return ""
        s = s.lower()
        s = re.sub(r"\s+", " ", s).strip()
        return s

    def train_from_dataframe(self, df: pd.DataFrame, message_col="creative_message", ctr_col="ctr") -> Dict[str, Any]:
        df = df.dropna(subset=[message_col, ctr_col])
        if len(df) < self.min_train:
            self.model = None
            self.vectorizer_fitted = False
            return {"status": "insufficient_data", "n_samples": int(len(df))}

        msgs = df[message_col].astype(str).tolist()
        y = df[ctr_col].astype(float).values

        self.vectorizer = TfidfVectorizer(max_features=self.tfidf_max, ngram_range=(1, 2), stop_words="english")
        X_tfidf = self.vectorizer.fit_transform([self._clean(m) for m in msgs])

        extra = pd.DataFrame({
            "len_chars": [len(m) for m in msgs],
            "len_words": [len(m.split()) for m in msgs],
            "exclamations": [count_exclamations(m) for m in msgs],
            "has_urgency": [1 if contains_urgency_words(m) else 0 for m in msgs],
            "has_discount": [1 if contains_discount(m) else 0 for m in msgs],
            "avg_tfidf": X_tfidf.mean(axis=1).A1
        })

        X_combined = np.hstack([X_tfidf.toarray(), extra.values])
        X_train, X_hold, y_train, y_hold = train_test_split(X_combined, y, test_size=0.15, random_state=self.seed)
        model = Ridge(alpha=1.0, random_state=self.seed)
        model.fit(X_train, y_train)

        self.model = model
        self.vectorizer_fitted = True
        self.feature_names = {
            "tfidf_vocabulary": list(self.vectorizer.get_feature_names_out()),
            "extra": list(extra.columns)
        }
        return {"status": "trained", "n_samples": int(len(df))}

    def _heuristic_score(self, msg: str) -> float:
        base = 0.01
        s = self._clean(msg)
        score = base
        if contains_urgency_words(s):
            score += 0.01
        if contains_discount(s):
            score += 0.01
        score += 0.0005 * len(s)
        score += 0.002 * min(count_exclamations(s), 3)
        return float(max(0.0, min(0.2, score)))

    def predict(self, messages: List[str]) -> List[Dict[str, Any]]:
        if not messages:
            return []
        if self.model is None or not self.vectorizer_fitted:
            out = []
            for m in messages:
                sc = self._heuristic_score(m)
                out.append({"message": m, "predicted_ctr": sc, "confidence": 0.45, "model": "heuristic"})
            return out

        cleaned = [self._clean(m) for m in messages]
        X_tfidf = self.vectorizer.transform(cleaned)
        extra = pd.DataFrame({
            "len_chars": [len(m) for m in cleaned],
            "len_words": [len(m.split()) for m in cleaned],
            "exclamations": [count_exclamations(m) for m in cleaned],
            "has_urgency": [1 if contains_urgency_words(m) else 0 for m in cleaned],
            "has_discount": [1 if contains_discount(m) else 0 for m in cleaned],
            "avg_tfidf": X_tfidf.mean(axis=1).A1
        })
        X_combined = np.hstack([X_tfidf.toarray(), extra.values])
        preds = self.model.predict(X_combined)
        preds = np.clip(preds, 0.0, 1.0)

        vocab = set(self.feature_names.get("tfidf_vocabulary", []))
        out = []
        for i, m in enumerate(cleaned):
            tokens = set(m.split())
            overlap = len(tokens & vocab)
            conf = min(0.95, 0.4 + 0.01 * overlap + 0.05 * extra.loc[i, "has_urgency"] + 0.05 * extra.loc[i, "has_discount"])
            out.append({
                "message": messages[i],
                "predicted_ctr": float(preds[i]),
                "confidence": float(conf),
                "model": "ml"
            })
        return out

    def simulate_batch(self, candidates_df: pd.DataFrame, message_col="creative_message", baseline_ctr: float = None) -> pd.DataFrame:
        msgs = candidates_df[message_col].astype(str).tolist()
        preds = self.predict(msgs)
        res = pd.DataFrame(preds)
        if baseline_ctr is None:
            baseline_ctr = 0.01
        res["improvement_vs_baseline"] = res["predicted_ctr"] - baseline_ctr
        res["pct_improvement"] = (res["improvement_vs_baseline"] / max(baseline_ctr, 1e-6)) * 100.0
        return candidates_df.reset_index(drop=True).join(res)
