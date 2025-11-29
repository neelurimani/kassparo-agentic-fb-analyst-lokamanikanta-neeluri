class InsightAgent:
    def __init__(self, cfg):
        self.cfg = cfg

    def generate(self, summary):
        hypotheses = [
            {"id": "H1", "text": "CTR decline may be causing ROAS drop", "confidence": 0.5},
            {"id": "H2", "text": "Audience fatigue due to repetitive creatives", "confidence": 0.5},
            {"id": "H3", "text": "Spend shifted into low-performing adsets", "confidence": 0.5}
        ]

        return {
            "summary": "Preliminary performance issues observed based on dataset.",
            "hypotheses": hypotheses
        }
