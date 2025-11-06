# Prompt Evaluation Framework for GenAI Models

A Python-based framework to test, evaluate, and score prompts against Generative AI (GenAI) models using AWS services. This project provides a structured approach to assess AI outputs for accuracy, completeness, and bias detection, making it ideal for QA, prompt evaluation, and AI validation tasks.

---

## 🚀 Project Overview

The **Prompt Evaluation Framework** allows users to:

- Run multiple prompts against GenAI models (AWS Bedrock / OpenAI-style APIs).
- Automatically score AI responses based on customizable metrics: accuracy, completeness, and bias.
- Store evaluation results in AWS services for analysis and reporting.
- Serve as a hands-on demonstration of GenAI QA workflows for portfolio purposes.

---

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **Cloud / Services:** AWS Lambda, S3, DynamoDB, Lambda Layers
- **Libraries / Utilities:** `boto3`, `requests`, custom scoring modules
- **Version Control:** Git & GitHub

---

## 📁 Project Structure

project_03_Prompt_Evaluation_Framework/
│
├── lambda_function.py # Main Lambda handler
├── utils/ # Utility functions for scoring & API calls
│ ├── bedrock_api.py
│ └── scoring.py
├── prompts.json # Sample prompts for evaluation
├── layer.zip # Lambda layer dependencies
└── README.md # Project documentation


---

## ✨ Features

- Evaluate multiple prompts efficiently.
- Scoring metrics include:
  - **Accuracy** – How closely the AI output matches expected results.
  - **Completeness** – Whether the AI output covers all required points.
  - **Bias Detection** – Detects potential bias in AI responses.
- Integrates seamlessly with AWS Lambda for serverless execution.
- Results can be stored in S3 or DynamoDB for reporting and analysis.

---

## ⚙️ Setup & Deployment

### Clone the repository
```bash
git clone <repo-url>
cd project_03_Prompt_Evaluation_Framework


Install dependencies
pip install -r requirements.txt

Prepare Lambda deployment package
zip -r lambda_function_deploy.zip lambda_function.py utils/

Update AWS Lambda function
aws lambda update-function-code \
    --function-name genai_prompt_eval \
    --zip-file fileb://lambda_function_deploy.zip

🧪 Usage / Testing

Go to AWS Lambda → genai_prompt_eval.

Configure a test event (JSON payload can be empty).

Click Test to run evaluation.

Check DynamoDB or S3 bucket for the results.

Sample Test Event:
{
  "test": "run"
}

📈 Future Improvements

Add support for multiple GenAI models simultaneously.

Enhance scoring metrics with semantic similarity and readability analysis.

Build a web dashboard for visualizing prompt evaluation results.

Add automated reporting & alerts for bias detection.

🧑‍💻 Author

Shailesh Gaikwad – QA / GenAI Tester

Portfolio-ready project demonstrating GenAI prompt evaluation and AWS serverless integration.




📄 License

This project is for portfolio and learning purposes. Feel free to explore and adapt for your own projects.


---

If you want, I can also **create a “Day-by-Day Portfolio Documentation”** with screenshots, AWS setup steps, and testing logs, which you can include as part of this README or a separate document for interviews.

