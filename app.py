import streamlit as st
import pandas as pd
import json
from preprocess import is_honeypot, passes_hard_filters
from rank import compute_composite_scores

st.title("🚀 Redrob AI Recruiter Sandbox")
st.write("Upload a candidate JSONL file to run the CPU-optimized filtering and ranking pipeline.")

jd_text = """
Senior AI/ML Engineer with 5-9 years of experience. 
Expertise in ranking systems, search retrieval, recommendation engines, or RAG pipelines.
Product company engineering background. Based in or willing to relocate to Pune/Noida.
"""

uploaded_file = st.file_uploader("Choose a candidates.jsonl file", type=["jsonl", "txt"])

if uploaded_file is not None:
    st.info("Processing candidates... please wait.")

    valid_candidates = []
    for line in uploaded_file:
        line_str = line.decode("utf-8").strip()
        if not line_str:
            continue
        cand = json.loads(line_str)
        
        if not is_honeypot(cand) and passes_hard_filters(cand):
            valid_candidates.append(cand)
            
    if len(valid_candidates) == 0:
        st.warning("No candidates passed the hard-qualification and honeypot filters.")
    else:
        results = compute_composite_scores(valid_candidates, jd_text)
        
        df = pd.DataFrame(results)
        df = df.sort_values(by=["score", "candidate_id"], ascending=[False, True]).reset_index(drop=True)
        df["rank"] = range(1, len(df) + 1)
        
        final_df = df[["candidate_id", "rank", "score", "reasoning"]].head(100)
        
        st.success(f"Successfully ranked the top {len(final_df)} candidates!")
        st.dataframe(final_df)
        
        csv = final_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Submission CSV",
            data=csv,
            file_name="sandbox_ranked_output.csv",
            mime="text/csv"
        )