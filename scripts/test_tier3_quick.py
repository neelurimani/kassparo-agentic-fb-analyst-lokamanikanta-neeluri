# scripts/test_tier3_quick.py
import pandas as pd
from src.agents.simulator import Simulator
from src.memory.memory import Memory
from src.utils.report_pdf import PdfReport
import yaml

cfg = yaml.safe_load(open("config/config.yaml"))
# synthetic tiny dataset
data = pd.DataFrame([
    {"creative_message": "Buy now — 20% OFF! Limited time", "ctr": 0.045},
    {"creative_message": "Huge sale — free delivery", "ctr": 0.039},
    {"creative_message": "Bestseller: comfy shoes", "ctr": 0.012},
    {"creative_message": "Shop today: ends soon", "ctr": 0.052},
    {"creative_message": "New arrivals", "ctr": 0.009},
] * 10)  # replicate to reach min samples

candidates = pd.DataFrame([
    {"campaign_name": "Spring Sale", "creative_message": "20% OFF Today Only — Shop Now!"},
    {"campaign_name": "Spring Sale", "creative_message": "Limited stock. Free returns within 30 days."},
    {"campaign_name": "Spring Sale", "creative_message": "Discover our best-selling collection"}
])

sim = Simulator(cfg)
print("Training:", sim.train_from_dataframe(data))
res = sim.simulate_batch(candidates)
print(res[["creative_message","predicted_ctr","confidence","pct_improvement"]])
mem = Memory(path=cfg.get("memory", {}).get("path", "memory/memory.json"))
mem.append_event({"type":"test_run", "note":"ran quick simulation"})
pdf = PdfReport().build("localtest01","Test Run","This is a quick test", [{"id":"H1","text":"CTR drop example","confidence":0.9}], [{"campaign_name":"S","headline":"20% OFF","predicted_ctr":0.03}], ["Action 1"])
print("PDF:", pdf)
