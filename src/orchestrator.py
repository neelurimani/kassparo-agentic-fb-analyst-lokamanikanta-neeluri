import pandas as pd
import uuid
from pathlib import Path

from src.agents.planner import PlannerAgent
from src.agents.data_agent import DataAgent
from src.agents.insight_agent import InsightAgent
from src.agents.evaluator_agent import EvaluatorAgent
from src.agents.creative_generator import CreativeAgent

from src.agents.simulator import Simulator
from src.memory.memory import Memory
from src.utils.report_pdf import PdfReport


class Orchestrator:
    def __init__(self, cfg):
        self.cfg = cfg
        self.planner = PlannerAgent(cfg)
        self.data_agent = DataAgent(cfg)
        self.insight_agent = InsightAgent(cfg)
        self.evaluator = EvaluatorAgent(cfg)
        self.creative_agent = CreativeAgent(cfg)

        Path("logs").mkdir(exist_ok=True)
        Path("reports").mkdir(exist_ok=True)
        Path("memory").mkdir(exist_ok=True)


    def run(self, query):
        print("\n=== PIPELINE START ===")

        # 1️⃣ Planner: break down tasks
        plan = self.planner.create_plan(query)
        print("Plan:", plan)

        # 2️⃣ Data Agent: load + summarize CSV
        df, summary = self.data_agent.load_and_summarize()
        print("Data loaded:", df.shape)

        # 3️⃣ Insight Agent: generate hypotheses
        insights = self.insight_agent.generate(summary)
        print("Generated hypotheses:", len(insights["hypotheses"]))

        # 4️⃣ Evaluator Agent: validate hypotheses
        validated = self.evaluator.validate(insights, df)
        print("Validated hypotheses.")

        # 5️⃣ Creative Generator: produce low CTR creatives
        creative_candidates = self.creative_agent.generate(df)
        print("Generated creative candidates:", len(creative_candidates))

        # 6️⃣ Tier-3 Simulator + Memory + PDF
        result = self.run_tier3(df, creative_candidates, validated)

        print("=== PIPELINE COMPLETE ===\n")
        return result


    # -----------------------------
    # Tier-3 Enhanced Pipeline
    # -----------------------------
    def run_tier3(self, df, creative_candidates, validated_insights):
        run_id = "run_" + uuid.uuid4().hex[:8]

        memory = Memory(self.cfg["memory"]["path"])
        sim = Simulator(self.cfg)

        # Train simulator
        train_info = sim.train_from_dataframe(df)
        memory.append_event({
            "type": "training",
            "info": train_info,
            "run_id": run_id
        })

        # Predict CTR for creative candidates
        predictions = sim.simulate_batch(creative_candidates)
        top_preds = predictions.sort_values("predicted_ctr", ascending=False).head(10)

        memory.remember(run_id + "_top_predictions", top_preds.to_dict(orient="records"))

        # Build PDF report
        pdf = PdfReport("reports").build(
            run_id=run_id,
            title="Agentic FB Performance Report",
            executive_summary=validated_insights["summary"],
            hypotheses=validated_insights["hypotheses"],
            creatives=top_preds.to_dict(orient="records"),
            actions=[
                "A/B Test top creatives",
                "Shift budget to high CVR placements",
                "Pause low CTR creatives"
            ]
        )

        return {
            "run_id": run_id,
            "sim_results": predictions.to_dict(orient="records"),
            "pdf_path": pdf
        }
