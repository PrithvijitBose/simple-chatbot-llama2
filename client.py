import requests
import streamlit as st
import os

# Enable LangSmith tracing (optional)
os.environ["LANGCHAIN_TRACING_V2"] = "true"
langsmith_key = os.getenv("LANGCHAIN_API_KEY")

def get_ollama_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/poem/invoke",
            json={"input": {"topic": input_text}},
        )
        response.raise_for_status()
        data = response.json()

        # If backend sends plain string
        if isinstance(data, str):
            return data

        # If backend sends dict
        return data.get("output", {}).get("content", "No content returned.")
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("Langchain Demo With LLAMA2 API")

topic = st.text_input("Write a poem on:")

if topic:
    with st.spinner("LLAMA2 is writing your poem..."):
        st.write(get_ollama_response(topic))
