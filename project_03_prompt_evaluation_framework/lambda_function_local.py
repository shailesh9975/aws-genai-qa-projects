import json

# Mock prompts (instead of reading from S3)
prompts = [
    {"prompt_id": "1", "prompt_text": "Explain photosynthesis."},
    {"prompt_id": "2", "prompt_text": "Summarize AI trends in 2025."},
    {"prompt_id": "3", "prompt_text": "Detect bias in this text."}
]

# Mock scoring function
def score_output(prompt, output):
    # Simple example: score 0.8 for all
    return 0.8

# Simulate Lambda handler
def lambda_handler(event=None, context=None):
    results = []
    for p in prompts:
        output = f"Generated response for: {p['prompt_text']}"
        score = score_output(p, output)
        results.append({
            "prompt_id": p["prompt_id"],
            "prompt_text": p["prompt_text"],
            "output": output,
            "score": score
        })
    return {"results": results}

# Run locally
if __name__ == "__main__":
    result = lambda_handler()
    print(json.dumps(result, indent=2))

