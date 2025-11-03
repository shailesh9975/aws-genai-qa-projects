import boto3
import json

# Initialize Bedrock Runtime client
client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

def lambda_handler(event, context):
    """AWS Lambda handler for Bedrock Claude model"""

    try:
        # Get prompt input from event or default
        prompt = event.get("prompt", "Explain what Generative AI QA testing means in simple terms.")

        model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"

        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 500,
            "messages": [{"role": "user", "content": prompt}],
        }

        # Call the model
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(body)
        )

        # Parse response
        result = json.loads(response["body"].read())

        answer = result["content"][0]["text"]

        return {
            "statusCode": 200,
            "body": json.dumps({"response": answer})
        }

    except client.exceptions.ThrottlingException:
        return {
            "statusCode": 429,
            "body": json.dumps({"error": "Too many requests. Try again later."})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

