# REDROB AI HACKATHON

A production-grade, CPU-optimized, two-stage intelligence engine engineered for the **Redrob INDIA RUNS Hackathon**. This system processes large-scale candidate datasets, screens out malicious data traps (honeypots), bypasses keyword-stuffing strategies, and ranks top-tier product-engineering talent entirely offline within a strict 5-minute compute runtime constraint.

---

# 📊 Pipeline Workflow

### Stage 1: Anti-Trap & Constraint Filtering

The candidate dataset is first validated to identify and remove suspicious or synthetic profiles.
**Operations performed:**
* Timeline validation
* Honeypot detection
* Geography filtering
* Years-of-experience filtering
**Outcome:** Reduces the search space from approximately 100,000 profiles to a manageable pool of highly relevant candidates.

---

### Stage 2: Semantic Search & Signal Blending

Eligible candidates are evaluated against the target job requirements using local semantic embeddings.

**Operations performed:**
* MiniLM embedding generation (`all-MiniLM-L6-v2`)
* Cosine similarity matching
* Behavioral signal weighting
* Composite score calculation

**Behavioral signals include:**
* Recruiter response rate
* Interview completion rate
* Platform engagement indicators

---

### Stage 3: Ranking & Validation

Candidates are ranked using the blended relevance score and validated against hackathon submission rules.
**Operations performed:**
* Candidate ranking
* Deterministic tie-breaking
* Reason generation
* Output validation

---

### Generated Deliverables

The pipeline automatically generates:

* `output.csv`
* `output.xlsx`

Both files are validated to ensure compliance with the competition submission requirements.

---

# 📁 Project Structure

redrob-ai/
│
├── preprocess.py
│   └── Honeypot detection and filtering
│
├── rank.py
│   └── Semantic ranking and score blending
│
├── main.py
│   └── Pipeline entrypoint
│
├── app.py
│   └── Streamlit dashboard
│
├── requirements.txt
│   └── Project dependencies
│
├── submission_metadata.yaml
│   └── Submission details
│
└── README.md
    └── Project documentation

---

# 🚀 Core Engineering Features

### 🛡️ Automated Honeypot Interception

Detects synthetic timeline anomalies and immediately excludes suspicious candidate profiles to prevent submission disqualification.

### 🧠 Context-Aware Semantic Matching

Uses lightweight local sentence-transformer embeddings (`all-MiniLM-L6-v2`) to evaluate candidate relevance beyond simple keyword matching.

### 📈 Dynamic Behavioral Signal Blending

Incorporates recruiter engagement indicators such as:

* Recruiter response rate
* Interview completion rate
* Platform activity signals

These signals are blended into the final ranking score using weighted multipliers.

### ⚡ CPU-Optimized Processing

Streams compressed `.jsonl` candidate datasets line-by-line using memory-efficient iterators to ensure fast execution under strict runtime constraints.

---

# 🛠️ Installation & Setup

## 1. Clone the Repository

git clone <https://github.com/codecmgit/redrob-ai.git>
cd redrob-ai

## 2. Install Dependencies

py -m pip install -r requirements.txt

## 3. Add Dataset Assets

Place the assigned dataset file in the project root:
candidates.jsonl

The file should reside alongside the main project scripts.

---

# ▶️ Running the Pipeline

## Local Batch Ranking

Update your Hack2Skill Participant ID inside `main.py` and execute:

python main.py

## Streamlit Sandbox Dashboard

Launch the local visualization dashboard:

py -m streamlit run app.py

---

# 📦 Expected Output

The pipeline automatically generates and validates the following submission files:

### 📄 output.csv

Competition-compliant output containing:

* Exactly 100 candidate rows
* Unique ranks from 1–100
* Proper sorting order
* Deterministic scoring
* Generated reasoning summaries

### 📊 output.xlsx

Spreadsheet version matching the CSV output for backup and review purposes.

---

# 🔍 Processing Workflow

1. Load candidate dataset from compressed JSONL source.
2. Detect and remove synthetic or suspicious profiles.
3. Apply hard eligibility filters.
4. Generate semantic embeddings locally.
5. Compute candidate-to-role relevance scores.
6. Blend recruiter and behavioral signals.
7. Rank candidates deterministically.
8. Generate explainable reasoning strings.
9. Validate output against hackathon requirements.
10. Export CSV and XLSX deliverables.

---

# 🎯 Design Goals

* Fully offline execution
* CPU-only compatibility
* Deterministic ranking outputs
* Fast processing for 100K+ profiles
* Robust protection against honeypot traps
* Explainable candidate recommendations

---

# 👨‍💻 Developed By

**Name:** Chirashree Mallick

**Hackathon:** Redrob INDIA RUNS Hackathon

**Technology Stack:** Python, Sentence Transformers, Pandas, NumPy, Streamlit