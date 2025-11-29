import pandas as pd

class DataAgent:
    def __init__(self, cfg):
        self.cfg = cfg
        self.path = cfg["data"]["path"]

    def load_and_summarize(self):
        df = pd.read_csv(self.path)

        summary = {
            "rows": len(df),
            "columns": list(df.columns),
            "avg_ctr": df["ctr"].mean(),
            "avg_roas": df["roas"].mean(),
            "campaigns": df["campaign_name"].nunique()
        }

        return df, summary
