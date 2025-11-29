from typing import Dict, Any, List
import pandas as pd


class CreativeAgent:
    def __init__(self, cfg):
        self.cfg = cfg

    def generate(self, df):
        low_ctr_df = df[df["ctr"] < df["ctr"].mean()]

        candidates = []
        for _, row in low_ctr_df.head(10).iterrows():
            msg = row["creative_message"]

            candidates.append({
                "campaign_name": row["campaign_name"],
                "creative_message": f"New idea inspired by: {msg}",
                "current_ctr": row["ctr"]
            })

        return pd.DataFrame(candidates)

class CreativeGenerator:
    def __init__(self, cfg: Dict[str, Any]):
        self.cfg = cfg

    def generate(self, df: pd.DataFrame, data_summary: Dict[str, Any]) -> Dict[str, Any]:
        df = df.copy()
        low_ctr_threshold = self.cfg["thresholds"]["low_ctr"]

        # compute campaign-level CTR
        camp_ctr = (
            df.groupby("campaign_name")
            .agg(
                impressions=("impressions", "sum"),
                clicks=("clicks", "sum"),
                ctr=("ctr", "mean")
            )
            .reset_index()
        )
        low_ctr_camps = camp_ctr[camp_ctr["ctr"] < low_ctr_threshold]

        recommendations = []
        candidates_rows = []

        for _, row in low_ctr_camps.iterrows():
            camp_name = row["campaign_name"]
            subset = df[df["campaign_name"] == camp_name]
            original_msgs = subset["creative_message"].dropna().unique().tolist()[:3]

            recs = []
            for msg in original_msgs:
                recs.append({
                    "id": f"{camp_name}_R1",
                    "headline": f"Limited Offer on {camp_name}",
                    "body": f"Shop now and get exclusive savings on {camp_name}.",
                    "cta": "Shop Now",
                    "rationale": "Adds urgency and benefit orientation.",
                    "confidence": 0.7
                })
                recs.append({
                    "id": f"{camp_name}_R2",
                    "headline": f"Customers love {camp_name}",
                    "body": "See why shoppers rate this so highly. Free returns and fast delivery.",
                    "cta": "Explore Bestsellers",
                    "rationale": "Adds social proof and lowers risk.",
                    "confidence": 0.65
                })
                candidates_rows.append({
                    "campaign_name": camp_name,
                    "creative_message": recs[-1]["headline"] + " " + recs[-1]["body"]
                })

            recommendations.append({
                "campaign_name": camp_name,
                "creative_type": subset["creative_type"].mode().iloc[0] if not subset["creative_type"].isna().all() else "unknown",
                "original_messages": original_msgs,
                "recommendations": recs
            })

        # baseline CTR
        baseline_ctr = df["ctr"].mean() if "ctr" in df.columns else 0.01
        candidates_df = pd.DataFrame(candidates_rows) if candidates_rows else pd.DataFrame(
            [{"campaign_name": "dummy", "creative_message": "Limited time offer. Shop now."}]
        )

        return {
            "campaign_recommendations": recommendations,
            "creatives_df": candidates_df,
            "baseline_ctr": float(baseline_ctr)
        }
