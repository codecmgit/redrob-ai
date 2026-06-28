import json
import gzip
import os

def is_honeypot(candidate):
    """
    Detects impossible synthetic data traps (Honeypots).
    If a candidate has data contradictions, flag them for disqualification.
    """
    profile = candidate.get("profile", {})
    history = candidate.get("career_history", [])
    signals = candidate.get("redrob_signals", {})
    
    years_claimed = profile.get("years_of_experience", 0)
    if years_claimed > 40:
        return True
    for job in history:
        duration = job.get("duration_months", 0)
        if duration < 0 or duration > 600:
            return True
    return False

def passes_hard_filters(candidate):
    """
    Applies the core Job Description criteria:
    - Experience: 4 to 11 years (Targeting the 5-9 target with a slight buffer)
    - Location: India (Pune, Noida, or major tech hubs)
    """
    profile = candidate.get("profile", {})
    country = str(profile.get("country", "")).strip().lower()
    location = str(profile.get("location", "")).strip().lower()
    yoe = profile.get("years_of_experience", 0)
    
    signals = candidate.get("redrob_signals", {})
    willing_to_relocate = signals.get("willing_to_relocate", False)
    
    is_india = country == "india" or "india" in location
    if not is_india and not willing_to_relocate:
        return False
        
    if yoe < 4.0 or yoe > 11.0:
        return False

    return True

def extract_and_filter_candidates(file_path):
    """
    Parses and extracts candidates from a .jsonl or .jsonl.gz file 
    without loading the entire massive file into memory all at once.
    """
    extracted_pool = []

    is_gzip = file_path.endswith('.gz')
    open_file = gzip.open if is_gzip else open
    file_mode = 'rt' if is_gzip else 'r'
    
    print(f"🔄 Opening dataset stream: {file_path}")
    
    with open_file(file_path, file_mode, encoding='utf-8') as stream:
        for index, line in enumerate(stream):
            if not line.strip():
                continue
                
            try:
                candidate_data = json.loads(line)

                if is_honeypot(candidate_data):
                    continue
                    
                if passes_hard_filters(candidate_data):
                    extracted_pool.append(candidate_data)
                    
            except json.JSONDecodeError:
                print(f"⚠️ Warning: Skipping corrupted row at line index {index}")
                continue
                
            if index % 10000 == 0 and index > 0:
                print(f"⚡ Stream checked {index} candidate lines...")
                
    print(f"✅ Data Extraction Complete. Extracted {len(extracted_pool)} compliant candidates.")
    return extracted_pool