# 🤖 Project 01 – AWS GenAI Chatbot using Bedrock (Claude + Streamlit + Lambda)

## 📚 Overview
This project demonstrates how to build a **Generative AI Chatbot** powered by **AWS Bedrock (Anthropic Claude 3.5 Sonnet)**.  
It allows real-time AI conversations using a **Streamlit frontend** and an **AWS Lambda backend** that securely calls the Bedrock Runtime API.

---

## 🧩 Project Structure
project_01_chatbot_bedrock/
│
├── app.py # Streamlit UI for local chat interaction
├── lambda_function.py # AWS Lambda backend function
├── test_bedrock_chatbot.py # Local test script to validate Bedrock connection
├── function.zip # Deployment package for Lambda
├── requirements.txt # Python dependencies
├── .gitignore # Ignore unnecessary files
└── README.md # Project documentation

User (Streamlit UI)
│
▼
AWS Lambda Function
│
▼
AWS Bedrock Runtime ──▶ Claude 3.5 Sonnet Model
│
▼
Returns AI response to Streamlit interface



---

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites
Before you start, make sure you have:
- Python **3.9+**
- An **AWS account** with **Bedrock access**
- IAM role with permission: `bedrock:InvokeModel`
- **Streamlit** installed locally

---

### 2️⃣ Local Environment Setup
Clone the repo:
```bash
git clone https://github.com/shailesh9975/aws-genai-qa-projects.git
cd aws-genai-qa-projects/project_01_chatbot_bedrock


python3 -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate



pip install -r requirements.txt

streamlit run app.py
Then open in your browser:
🌐 http://localhost:8501

Ask questions like:

“What is Generative AI QA testing?”

“Explain AWS Bedrock in simple terms.”

🧠 Lambda Deployment
Step 1: Prepare Deployment Package
zip -r function.zip lambda_function.py

Step 2: Deploy on AWS Lambda

Go to AWS Console → Lambda → Create Function

Choose “Author from scratch”

Runtime: Python 3.10

Upload function.zip

Set environment variables (if needed)

Attach IAM role with bedrock:InvokeModel permission

🧪 Local Testing

Run:

python test_bedrock_chatbot.py


Sample Output:

🤖 Claude Response:
Generative AI QA testing ensures the quality and reliability of AI systems that generate content...

📊 Key Learnings

✅ How to invoke AWS Bedrock models via boto3
✅ Building a Streamlit-based GenAI frontend
✅ Structuring cloud-based AI inference pipelines
✅ Testing and validating Claude model outputs for QA

🌍 Future Enhancements

 Add multi-model support (Claude, Titan, Llama)

 Integrate conversation history with DynamoDB

 Deploy Streamlit app on AWS EC2 or Streamlit Cloud

 Add prompt evaluation metrics for GenAI QA

👨‍💻 Author

Shailesh Gaikwad
QA Engineer | AI/ML Validation | GenAI QA Tester
🔗 GitHub
 | LinkedIn

“Testing AI is the art of teaching machines to think better.” 🧠

