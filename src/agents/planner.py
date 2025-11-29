class PlannerAgent:
    def __init__(self, cfg):
        self.cfg = cfg

    def create_plan(self, query):
        return {
            "query": query,
            "steps": [
                "load_data",
                "summarize_data",
                "generate_insights",
                "validate_insights",
                "generate_creatives",
                "simulate_creatives",
                "build_report"
            ]
        }
