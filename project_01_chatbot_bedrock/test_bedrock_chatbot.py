import boto3
import json

# Initialize Bedrock Runtime client
client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# Define model and prompt
model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"

prompt = "Explain what Generative AI QA testing means in simple terms."

# Prepare body
body = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 500,
    "messages": [
        {"role": "user", "content": prompt}
    ]
}

# Invoke model
response = client.invoke_model(
    modelId=model_id,
    body=json.dumps(body)
)

# Read and display model output
result = json.loads(response["body"].read())
print("\n🤖 Claude Response:\n")
print(result["content"][0]["text"])

