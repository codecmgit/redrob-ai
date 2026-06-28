import os
import json
from preprocess import extract_and_filter_candidates  
from rank import compute_composite_scores, generate_submission_files

def main():
    input_data_path = "candidates.jsonl" 
    output_filename = "synapse_syndicate_output" 
    
    job_description = """
    Looking for a Senior AI/ML Engineer with 5-9 years of experience. 
    Must have hands-on experience building and deploying ranking systems, search retrieval, 
    recommendation engines, or RAG pipelines. Strong engineering background in product companies. 
    Location: Pune, Noida, or major tech hubs in India.
    """
    
    if not os.path.exists(input_data_path):
        print(f"Error: Could not find input file '{input_data_path}' in this directory.")
        return

    filtered_candidates = extract_and_filter_candidates(input_data_path)
   
    scored_profiles = compute_composite_scores(filtered_candidates, job_description)
    
    generate_submission_files(scored_profiles, output_filename=output_filename)
    
    print("\n All pipeline execution steps completed successfully!")

if __name__ == "__main__":
    main()