# REDROB AI HACKATHON

A production-grade, CPU-optimized, two-stage intelligence engine engineered for the **Redrob INDIA RUNS Hackathon**. This system processes large-scale candidate datasets, screens out malicious data traps (honeypots), bypasses keyword-stuffing strategies, and ranks top-tier product-engineering talent entirely offline within a strict 5-minute compute runtime constraint.

---

# 📊 Pipeline System Architecture

[ Raw Input Data: candidates.jsonl ]
                  │
                  ▼
┌────────────────────────────────────────────────────────┐
│ STAGE 1: Offline Anti-Trap & Constraint Filtering      │
│                                                        │
│ • Timeline validation drops impossible honeypots       │
│ • Hard filters for target geographies and YOE          │
│ • Reduces processing space from 100K to ~1,000         │
└────────────────────────────────────────────────────────┘
                  │
                  ▼
┌────────────────────────────────────────────────────────┐
│ STAGE 2: Local Semantic Search & Signal Blending       │
│                                                        │
│ • Fast CPU embeddings via all-MiniLM-L6-v2             │
│ • Cosine similarity against job intent                 │
│ • Behavioral signal weighting and score blending       │
└────────────────────────────────────────────────────────┘
                  │
                  ▼
┌────────────────────────────────────────────────────────┐
│ STAGE 3: Post-Processing & Compliance Validation       │
│                                                        │
│ • Alphabetical tie-breaking                            │
│ • Deterministic reasoning generation                   │
│ • Submission format verification                       │
└────────────────────────────────────────────────────────┘
                  │
                  ▼
[ Verified Deliverables: synapse_syndicate.csv & synapse_syndicate.xlsx ]

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

### 📄 YOUR_PARTICIPANT_ID.csv

Competition-compliant output containing:

* Exactly 100 candidate rows
* Unique ranks from 1–100
* Proper sorting order
* Deterministic scoring
* Generated reasoning summaries

### 📊 YOUR_PARTICIPANT_ID.xlsx

Spreadsheet version matching the CSV output for backup and review purposes.

---

# 📁 Project Structure

redrob-ai/
│
├── preprocess.py             # Honeypot detection and filtering
├── rank.py                   # Semantic ranking and signal blending
├── main.py                   # Pipeline entrypoint
├── app.py                    # Streamlit sandbox dashboard
│
├── requirements.txt          # Dependency definitions
├── submission_metadata.yaml  # Team and submission metadata
└── README.md                 # Project documentation

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

**Team Name:** [Synapse Syndicate]

**Hackathon:** Redrob INDIA RUNS Hackathon

**Technology Stack:** Python, Sentence Transformers, Pandas, NumPy, Streamlit