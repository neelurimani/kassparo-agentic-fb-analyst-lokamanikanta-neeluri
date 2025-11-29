A fully autonomous, multi-agent AI system that diagnoses Facebook Ads performance, explains ROAS fluctuations, generates improved creative ideas, simulates CTR uplift using machine learning, and produces a PDF report for marketers.

This project extends the original assignment with a Tier-3 Enterprise Layer, including trend breakpoints, causal influence modeling, and creative clustering.

⭐ Features
✔ End-to-end Agentic Workflow

Planner → Data → Insight → Evaluator → Creative → Simulator → PDF Report → Enterprise Analytics

✔ ROAS Change Diagnosis

Automatically identifies why performance is dropping:

CTR decline

Creative fatigue

Bad audience match

Spend inefficiency

✔ Creative Generator

Creates new creative messages grounded in your dataset.

✔ CTR Uplift Simulation

Predicts how new creatives will perform using:

TF-IDF text vectorization

Linear Regression CTR model

✔ PDF Report Generation

A ready-to-share executive summary PDF.

✔ Enterprise Analytics

Breakpoint detection (trend anomalies)

Causal engine (CTR → ROAS, Spend → ROAS)

Creative message clusters (KMeans)

JSON-based analytics reports

🧠 System Architecture
🔧 High-Level Architecture Diagram (Mermaid)
flowchart TD

A[run.py] --> B[Planner Agent]
B --> C[Data Agent]
C --> D[Insight Agent]
D --> E[Evaluator Agent]
E --> F[Creative Generator Agent]
F --> G[CTR Simulator (ML Model)]
G --> H[PDF Report Generator]
H --> I[Enterprise Tier Analytics]

I --> I1(Breakpoint Detection)
I --> I2(Causal Engine)
I --> I3(Creative Clustering)

📂 Project Structure
Kasparro Agentic FB Analyst/
│
├── run.py
├── README.md
├── requirements.txt
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── facebook_ads.csv
│   └── README.md
│
├── reports/
│   ├── dashboard_<run_id>.pdf
│   └── enterprise/
│        ├── breakpoints_<run_id>.json
│        ├── causal_ctr_<run_id>.json
│        ├── causal_spend_<run_id>.json
│        ├── clusters_<run_id>.json
│
├── src/
│   ├── orchestrator.py
│   ├── agents/
│   │   ├── planner.py
│   │   ├── data_agent.py
│   │   ├── insight_agent.py
│   │   ├── evaluator_agent.py
│   │   ├── creative_generator.py
│   │   └── simulator.py
│   ├── enterprise/
│   │   ├── breakpoint_detector.py
│   │   ├── causal_engine.py
│   │   └── clustering.py
│   ├── utils/
│   │   └── report_pdf.py
│   └── memory/
│       └── memory.py
│
└── logs/

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/kasparro-agentic-fb-analyst-manikanta-neeluri.git
cd kasparro-agentic-fb-analyst-manikanta-neeluri

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Agentic System
python run.py "Analyze ROAS drop"

🏃 Pipeline Execution Flow

When you run:

python run.py "Analyze ROAS drop"


The following happens:

Planner Agent creates plan

Data Agent loads dataset

Insight Agent produces hypotheses

Evaluator Agent validates with metrics

Creative Agent generates new creatives

Simulator predicts CTR uplift

PDF report is generated

Enterprise analytics run:

Breakpoint detection

CTR & spend causal influence

Creative clustering

📊 Example Output
✔ Simulated Creative Performance
predicted_ctr: 0.0150
pct_improvement: +50.11%
confidence: 0.49

✔ PDF Saved
reports/dashboard_run_ab4cfd11.pdf

✔ Enterprise Outputs
reports/enterprise/breakpoints_run_ab4cfd11.json
reports/enterprise/causal_ctr_run_ab4cfd11.json
reports/enterprise/clusters_run_ab4cfd11.json

🔥 Enterprise Tier Breakdown
📈 Breakpoint Detection

Finds trend anomalies in CTR/ROAS using rolling z-scores.

Example:

ROAS drop detected on 2023-06-14 (z = -3.2)

🧭 Causal Engine

Estimates the directional impact of variables like:

CTR → ROAS

Spend → ROAS

Example:

CTR → ROAS causal coefficient = +0.83 (confidence: 0.91)

🎨 Creative Clustering

Groups creatives based on message similarity.

Example:

Cluster 3 = Highest CTR (0.0182)
Keywords: cotton, breathable, cooling

💾 Memory System

Stores:

Best creatives

Training summaries

Event logs

Past run performance

Stored inside:

memory/memory.json

🧪 Testing

Tests for:

Evaluator Agent

Simulator Model

Enterprise Causal Engine

Breakpoint detection stability

Run:

pytest tests/

