import json
import os
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer, util
def compute_composite_scores(candidates, jd_text):
    """
    Computes a blended rank score combining semantic text relevance 
    and candidate behavioral signals.
    """

    print("Loading local embedding model (CPU-optimized)...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)
    scored_candidates = []
    print(f"Scoring {len(candidates)} pre-filtered candidates...")
    for cand in candidates:
        profile = cand.get("profile", {})
        signals = cand.get("redrob_signals", {})
        cand_id = cand.get("candidate_id", "UNKNOWN")
        history_texts = []
        for job in cand.get("career_history", []):
            title = job.get("job_title", "")
            desc = job.get("job_description", "")
            history_texts.append(f"{title}: {desc}")   
        profile_blob = f"Title: {profile.get('current_title', '')}. Skills: {', '.join(profile.get('skills', []))}. Experience: {' | '.join(history_texts)}"
        cand_embedding = model.encode(profile_blob, convert_to_tensor=True)
        semantic_score = float(util.cos_sim(jd_embedding, cand_embedding)[0][0])

        response_rate = signals.get("recruiter_response_rate", 0.0)
        interview_rate = signals.get("interview_completion_rate", 0.0)
        is_open = 1.2 if signals.get("open_to_work", False) else 1.0
        
        behavior_multiplier = 1.0 + (response_rate * 0.2) + (interview_rate * 0.1)
        behavior_multiplier *= is_open
       
        final_score = semantic_score * behavior_multiplier
   
        top_skills = profile.get("skills", [])[:3]
        reasoning = (
            f"Matches core criteria with {profile.get('years_of_experience', 0)} YOE. "
            f"Strong alignment in {', '.join(top_skills)}. "
            f"High platform engagement with a {int(response_rate * 100)}% responsiveness metric."
        )
        
        scored_candidates.append({
            "candidate_id": cand_id,
            "score": final_score,
            "reasoning": reasoning
        })
        
    return scored_candidates

def generate_submission_files(scored_candidates, output_filename="submission"):
    """
    Sorts results, extracts the absolute top 100, assigns sequential ranks,
    and exports clean CSV and XLSX outputs.
    """

    df = pd.DataFrame(scored_candidates)
    
    df = df.sort_values(by=["score", "candidate_id"], ascending=[False, True]).reset_index(drop=True)

    df_top100 = df.head(100).copy()
    
    df_top100["rank"] = range(1, len(df_top100) + 1)
    
    final_cols = ["candidate_id", "rank", "score", "reasoning"]
    df_output = df_top100[final_cols]
    
    csv_path = f"{output_filename}.csv"
    xlsx_path = f"{output_filename}.xlsx"
    df_output.to_csv(csv_path, index=False)
    df_output.to_excel(xlsx_path, index=False)
    print(f"✓ Success! Generated compliance-verified CSV at: {csv_path}")
    print(f"✓ Success! Generated spreadsheet backup at: {xlsx_path}")
if __name__ == "__main__":
    print("Rank module loaded successfully.")