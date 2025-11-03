<<<<<<< HEAD
# 🧠 AWS GenAI QA Projects

### 👨‍💻 Author: [Shailesh Gaikwad](https://www.linkedin.com/in/shaileshgaikwad9975/)
> QA Engineer (Manual · ADAS · AI/ML Testing)  
> Transitioning into **GenAI QA / Prompt Evaluation / AI Quality Engineering**

---

## 📘 Overview
This repository contains a collection of **end-to-end AWS + GenAI QA projects**, designed to demonstrate real-world skills in **AI Testing**, **Prompt Evaluation**, and **Cloud QA Automation**.

All projects are tested locally using **Streamlit** and deployed with **AWS Bedrock**, **Lambda**, and **S3** services.

---

## 📂 Project List

### 🧩 [Project 01 – GenAI Chatbot (Claude 3.5 Sonnet)](project_01_chatbot_bedrock)
> Build and test a **Generative AI Chatbot** using **AWS Bedrock (Claude 3.5)** and **Streamlit UI**.  
> Includes QA evaluation to assess **clarity, accuracy, and relevance** of AI responses.

🔹 Tech: `AWS Bedrock`, `Streamlit`, `boto3`, `Python`  
🔹 Focus: *GenAI QA, Prompt Evaluation, Bedrock API Testing*

---

### 📄 [Project 02 – AI Document Summarizer (Bedrock + Lambda + S3)](project_02_summarizer_lambda)
> Automatically generate **summaries** for uploaded documents stored in S3.  
> Uses AWS Lambda for automation and Claude for summarization.

🔹 Tech: `AWS Lambda`, `S3`, `Bedrock`, `Python`  
🔹 Focus: *Automation, File I/O Testing, Response Validation*

---

### 💬 [Project 03 – Prompt Evaluation Framework](project_03_prompt_eval_framework)
> Test multiple prompts against GenAI models and evaluate outputs.  
> Includes scoring metrics for **accuracy**, **completeness**, and **bias** detection.

🔹 Tech: `Python`, `Bedrock`, `OpenAI Eval style`  
🔹 Focus: *Prompt QA Evaluation, Test Automation, Scoring Systems*

---

### 🔍 [Project 04 – RAG QnA System (Retrieval-Augmented Generation)](project_04_rag_qna_system)
> Integrates AWS Bedrock with vector search for **document-based QnA**.  
> Tests how retrieval quality impacts GenAI answer accuracy.

🔹 Tech: `Bedrock`, `LangChain`, `FAISS`, `Python`  
🔹 Focus: *RAG Testing, Context Evaluation, Precision/Recall QA*

---

### ⚖️ [Project 05 – Multi-Model Evaluation System](project_05_multi_model_eval)
> Compare responses from multiple GenAI models (Claude, Titan, Llama) side-by-side.  
> Evaluate performance across different QA metrics.

🔹 Tech: `AWS Bedrock`, `Python`, `Streamlit`  
🔹 Focus: *Model Comparison, Response Benchmarking, QA Metrics*

---

### 🧠 [Project 06 – Human Feedback Evaluation System](project_06_human_feedback_system)
> Implements a **human-in-the-loop QA feedback system** for GenAI outputs.  
> Collects user feedback (👍👎) and updates model evaluation scores.

🔹 Tech: `Streamlit`, `Bedrock`, `CSV Storage`, `Python`  
🔹 Focus: *RLHF Simulation, Feedback QA, Continuous Improvement*

---

## 📈 Learning Goals
Each project builds progressively to strengthen your skills in:
- ✅ Manual & Exploratory Testing of GenAI Systems  
- ✅ Prompt Evaluation & Quality Metrics  
- ✅ AWS Bedrock Integration & Cloud QA  
- ✅ AI Output Validation (Accuracy, Clarity, Relevance)  
- ✅ Test Automation with Python  

---

## 🧰 Tech Stack Summary
| Category | Tools / Services |
|-----------|------------------|
| **Cloud / AI** | AWS Bedrock, Lambda, S3 |
| **Models** | Claude 3.5 Sonnet, Titan Text |
| **Frameworks** | Streamlit, LangChain |
| **Languages** | Python (boto3, json) |
| **QA Tools** | Manual QA, Prompt Testing, Evaluation Metrics |

---

## 📜 License
This repository is for **learning and portfolio demonstration purposes**.  
Feel free to fork or adapt for educational use with attribution.

---

## 🏁 Next Steps
Coming Soon:
- 🧩 Project 07 – Automated Prompt Regression Testing  
- 📊 Project 08 – GenAI Performance Benchmark Dashboard  

---

**⭐ If you find this useful, give the repo a star and connect with me on LinkedIn!**  
> _“Testing AI is the art of teaching machines to think better.”_

=======
🤖 Project 01 – AWS GenAI Chatbot using Bedrock (Claude + Streamlit + Lambda)
📚 Overview

This project demonstrates how to build a Generative AI Chatbot powered by AWS Bedrock (Anthropic Claude model).
The chatbot allows users to interact with an AI model in real-time using a Streamlit frontend, while the AWS Lambda backend handles inference requests securely through Bedrock Runtime.

🧩 Project Structure
project_01_chatbot_bedrock/
│
├── app.py                      # Streamlit UI for local chat interaction
├── lambda_function.py          # AWS Lambda backend function
├── test_bedrock_chatbot.py     # Local test script to validate Bedrock connection
├── function.zip                # Deployment package for Lambda
├── requirements.txt            # Project dependencies
├── .gitignore                  # Ignore unnecessary files
└── README.md                   # Project documentation

☁️ Architecture
User (Streamlit UI)
       │
       ▼
AWS Lambda Function  ──▶  AWS Bedrock Runtime  ──▶  Claude 3.5 Sonnet Model
       │
       ▼
  Returns AI response to Streamlit

⚙️ Setup Instructions
1️⃣ Prerequisites

Python 3.9+

AWS Account with Bedrock access

IAM role with bedrock:InvokeModel permission

Streamlit installed locally

2️⃣ Local Environment Setup
# Clone the repo
git clone https://github.com/shailesh9975/aws-genai-qa-projects.git
cd aws-genai-qa-projects/project_01_chatbot_bedrock

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

3️⃣ Run Locally with Streamlit
streamlit run app.py


Then open in your browser:
🌐 http://localhost:8501

You’ll see a chat interface where you can ask questions like:

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

🧪 Testing Locally
python test_bedrock_chatbot.py


Sample Output:

🤖 Claude Response:
Generative AI QA testing ensures quality and reliability of AI systems that create content...

📊 Key Learnings

How to invoke AWS Bedrock models via boto3

Building a Streamlit-based GenAI frontend

Structuring cloud-based AI inference pipelines

Testing and validating Claude model outputs for QA

🌍 Future Enhancements

✅ Add multi-model support (Claude, Titan, Llama)
✅ Integrate conversation history persistence (DynamoDB)
✅ Deploy Streamlit app on AWS EC2 or Streamlit Cloud

👨‍💻 Author

Shailesh Gaikwad
QA Engineer | AI/ML Validation | GenAI QA Tester
🔗 GitHub | LinkedIn
>>>>>>> 93e07d9 (🚀 Added AWS GenAI Chatbot Project (Claude + Streamlit + Lambda))
