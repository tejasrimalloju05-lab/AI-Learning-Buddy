import streamlit as st
import google.generativeai as genai
import os

# Page configuration
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Learning Buddy")
st.write("An AI-powered learning assistant for interactive learning.")

# Gemini API configuration
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key is not configured.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# Topic
topic = st.text_input(
    "📚 Enter a topic",
    "Machine Learning Fundamentals"
)

st.write("You selected:", topic)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Ask me something about your topic...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    prompt = f"""
You are an AI Learning Buddy.

The student's selected topic is:
{topic}

Answer the student's question clearly and in a beginner-friendly way.

Student question:
{user_input}

Include an example when useful.
"""

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.generate_content(prompt)
            answer = response.text

        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
