import os
import json
import logging
from decimal import Decimal
import boto3
from botocore.exceptions import ClientError

# Import utility functions
try:
    from utils.bedrock_api import call_bedrock_model
    from utils.scoring import evaluate_output
except ImportError:
    # fallback mock functions if utils not present
    def call_bedrock_model(prompt):
        return f"Generated response for: {prompt.get('text')}"

    def evaluate_output(prompt, output):
        if prompt.get('expected_answer') and prompt['expected_answer'] in output:
            return 1.0
        return 0.5

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# AWS clients
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

# Environment variables
PROMPT_BUCKET = os.environ.get('PROMPT_BUCKET')
PROMPT_FILE_KEY = os.environ.get('PROMPT_FILE_KEY')
RESULT_BUCKET = os.environ.get('RESULT_BUCKET')  # optional
DYNAMO_TABLE = os.environ.get('DYNAMO_TABLE')

if not PROMPT_BUCKET or not PROMPT_FILE_KEY or not DYNAMO_TABLE:
    raise ValueError("PROMPT_BUCKET, PROMPT_FILE_KEY, or DYNAMO_TABLE environment variable not set.")

table = dynamodb.Table(DYNAMO_TABLE)

def lambda_handler(event, context):
    logger.info("Lambda triggered for prompt evaluation.")

    # Step 1: Read prompts from S3
    try:
        logger.info(f"Reading prompts from S3: {PROMPT_BUCKET}/{PROMPT_FILE_KEY}")
        response = s3_client.get_object(Bucket=PROMPT_BUCKET, Key=PROMPT_FILE_KEY)
        prompts = json.loads(response['Body'].read().decode('utf-8'))
        logger.info(f"Total prompts fetched: {len(prompts)}")
    except ClientError as e:
        logger.error(f"Failed to read prompts from S3: {e}")
        return {"statusCode": 500, "body": f"Error reading prompts: {str(e)}"}
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in prompts file: {e}")
        return {"statusCode": 500, "body": f"Invalid JSON: {str(e)}"}

    results = []

    # Step 2: Process each prompt
    for prompt in prompts:
        prompt_id = prompt.get('id', 'unknown')
        logger.info(f"Processing prompt ID: {prompt_id}")

        try:
            # Call LLM (mock or actual Bedrock)
            output_text = call_bedrock_model(prompt)
            score = evaluate_output(prompt, output_text)
        except Exception as e:
            logger.exception(f"Error generating output for prompt {prompt_id}")
            output_text = ""
            score = 0.0

        # Step 3: Prepare item for DynamoDB (convert floats to Decimal)
        item = {
            'prompt_id': str(prompt_id),
            'prompt_text': prompt.get('text', ''),
            'output': output_text,
            'score': Decimal(str(score))  # DynamoDB requires Decimal, not float
        }

        # Save to DynamoDB
        try:
            table.put_item(Item=item)
            logger.info(f"Saved prompt {prompt_id} to DynamoDB table: {DYNAMO_TABLE}")
        except ClientError as e:
            logger.error(f"Failed to save prompt {prompt_id} to DynamoDB: {e}")

        # Step 4: Optionally save result to S3
        if RESULT_BUCKET:
            try:
                import datetime
                timestamp = datetime.datetime.utcnow().isoformat()
                result_key = f"results/{prompt_id}_{timestamp}.json"
                s3_client.put_object(
                    Bucket=RESULT_BUCKET,
                    Key=result_key,
                    Body=json.dumps(item, default=str).encode('utf-8')
                )
                logger.info(f"Saved prompt {prompt_id} output to S3: {RESULT_BUCKET}/{result_key}")
            except ClientError as e:
                logger.error(f"Failed to save prompt {prompt_id} to S3: {e}")

        results.append(item)

    logger.info("Lambda execution completed successfully.")
    return {"statusCode": 200, "body": json.dumps({"results": results}, default=str)}




if __name__ == "__main__":
    import json
    # Simulate Lambda event
    event = {}
    result = lambda_handler(event, None)
    print(json.dumps(result, indent=2))

