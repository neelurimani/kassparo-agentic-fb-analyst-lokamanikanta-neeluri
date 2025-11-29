class EvaluatorAgent:
    def __init__(self, cfg):
        self.cfg = cfg

    def validate(self, insights, df):
        validated = []

        for h in insights["hypotheses"]:
            # If hypothesis mentions CTR, use CTR↔ROAS correlation
            if "CTR" in h["text"]:
                conf = abs(df["ctr"].corr(df["roas"]))
            else:
                # Default moderate confidence
                conf = 0.6

            validated.append({
                "id": h["id"],
                "text": h["text"],
                "confidence": round(conf, 3)
            })

        return {
            "summary": insights["summary"],
            "hypotheses": validated
        }
