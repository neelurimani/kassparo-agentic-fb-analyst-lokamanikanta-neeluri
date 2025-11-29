import pandas as pd

from src.agents.simulator import Simulator


def test_simulator_train_and_predict():
    cfg = {"simulator": {"min_train_samples": 5, "tfidf_max_features": 100, "random_seed": 42}}
    data = pd.DataFrame(
        [
            {"creative_message": "Buy now 20% off!", "ctr": 0.04},
            {"creative_message": "Limited time sale", "ctr": 0.03},
            {"creative_message": "New arrivals", "ctr": 0.01},
            {"creative_message": "Free delivery today", "ctr": 0.05},
            {"creative_message": "Shop now", "ctr": 0.02},
        ]
    )
    sim = Simulator(cfg)
    info = sim.train_from_dataframe(data)
    assert info["status"] == "trained"
    res = sim.predict(["Huge 30% OFF today", "Just browse our catalog"])
    assert len(res) == 2
    assert all(0.0 <= r["predicted_ctr"] <= 1.0 for r in res)
