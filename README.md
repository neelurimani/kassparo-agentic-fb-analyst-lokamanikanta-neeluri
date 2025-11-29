# 🚀 Kasparro Agentic Facebook Performance Analyst – Enterprise Edition


A fully autonomous, multi-agent AI system that diagnoses Facebook Ads performance, explains ROAS fluctuations, generates improved creative ideas, simulates CTR uplift using machine learning, and produces a PDF report for marketers.

This project extends the original assignment with a **Tier-3 Enterprise Layer**, including trend breakpoints, causal influence modeling, and creative clustering.

---

# ⭐ Features

### ✔ End-to-end Agentic Workflow
Planner → Data → Insight → Evaluator → Creative → Simulator → PDF Report → Enterprise Analytics

### ✔ ROAS Change Diagnosis
Automatically identifies why performance is dropping:
- CTR decline
- Creative fatigue
- Bad audience match
- Spend inefficiency

### ✔ Creative Generator
Creates **new creative messages** grounded in your dataset.

### ✔ CTR Uplift Simulation
Predicts how new creatives will perform using:
- TF-IDF vectorization
- Linear Regression (CTR prediction)

### ✔ PDF Report Generation
A ready-to-share marketer-friendly summary.

### ✔ Enterprise Analytics
- Breakpoint detection (trend anomalies)
- Causal influence estimation
- Creative clustering (KMeans)
- JSON-based analytics outputs

---

# 🧠 System Architecture

## 🔧 High-Level Architecture Diagram (Mermaid)

```mermaid
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
```

---

# 📂 Project Structure

```
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
│        └── clusters_<run_id>.json
│
├── memory/
│   └── memory.json
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
```

---

# ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/kasparro-agentic-fb-analyst-manikanta-neeluri.git
cd kasparro-agentic-fb-analyst-manikanta-neeluri
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Agentic System

```bash
python run.py "Analyze ROAS drop"
```

---

# 🏃 Pipeline Execution Flow

When you run:

```
python run.py "Analyze ROAS drop"
```

✔ The Planner creates a plan  
✔ Data Agent loads & summarizes dataset  
✔ Insight Agent generates hypotheses  
✔ Evaluator creates confidence scores  
✔ Creative Agent generates improved ads  
✔ Simulator predicts CTR uplift  
✔ PDF Report is generated  
✔ Enterprise analytics are executed

---

# 📊 Example Output

### ✔ Simulated Creative Performance

```
predicted_ctr: 0.0150
pct_improvement: +50.11%
confidence: 0.49
```

### ✔ PDF Saved

```
reports/dashboard_run_ab4cfd11.pdf
```

### ✔ Enterprise Outputs

```
reports/enterprise/breakpoints_run_ab4cfd11.json
reports/enterprise/causal_ctr_run_ab4cfd11.json
reports/enterprise/clusters_run_ab4cfd11.json
```

---

# 🔥 Enterprise Tier Breakdown

## 📈 Breakpoint Detection
Finds anomalies in ROAS/CTR trends using rolling z-scores.

Example:
```
ROAS drop detected on 2023-06-14 (z = -3.2)
```

---

## 🧭 Causal Engine
Estimates directional influence of:

- CTR → ROAS  
- Spend → ROAS  

Example:
```
CTR → ROAS causal coefficient = +0.83 (confidence: 0.91)
```

---

## 🎨 Creative Clustering
Groups creatives based on TF-IDF message similarity.

Example:
```
Cluster 3 = Highest CTR (0.0182)
Keywords: cotton, breathable, cooling
```

---

# 💾 Memory System

Stores:

- best creatives  
- training metadata  
- run outputs  
- event logs  

Stored here:

```
memory/memory.json
```

---

# 🧪 Testing

```bash
pytest tests/
```

---

# 🛑 Assignment Requirements Covered

✔ insights.json  
✔ creatives.json  
✔ PDF report  
✔ Enterprise analytics  
✔ Proper logs  
✔ 3+ commits + v1.0 release  
✔ Clean folder structure  
✔ CLI runnable (`python run.py`)  
✔ Full agentic pipeline  

---

# 👨‍💻 Author

**Manikanta Neeluri**  
Applied AI Engineer – Kasparro Assignment  
India 🇮🇳

---

# 📜 License

MIT License

