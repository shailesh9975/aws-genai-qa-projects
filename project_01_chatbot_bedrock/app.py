import streamlit as st
import boto3
import json

# --- AWS Bedrock Setup ---
client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")
model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"

# --- Streamlit UI ---
st.title("🤖 AWS GenAI Chatbot - Claude (Bedrock)")
st.write("Chat with an Anthropic Claude model deployed via AWS Bedrock.")

# --- Initialize session state ---
if "messages" not in st.session_state:
    st.session_state.messages = []  # Initialize empty list for chat history

# --- Display previous chat messages ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Chat input ---
prompt = st.chat_input("Ask something about AI, QA, or AWS...")

if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Call Claude model ---
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 500,
        "temperature": 0.7,
        "messages": [{"role": "user", "content": prompt}],
    }

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.invoke_model(
                modelId=model_id,
                body=json.dumps(body)
            )
            # Read and parse model output
            result = json.loads(response["body"].read())
            output = result["content"][0]["text"]
            st.markdown(output)

    # --- Add Claude’s response to session state ---
    st.session_state.messages.append({"role": "assistant", "content": output})

