import streamlit as st
import google.generativeai as genai

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Learning Buddy")
st.write("An AI-powered learning assistant for interactive learning.")

# -----------------------------
# Gemini API Configuration
# -----------------------------
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key is not configured.")
    st.info("Please set the GEMINI_API_KEY in Streamlit secrets.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------
# Topic Selection
# -----------------------------
topic = st.text_input(
    "📚 Enter a topic",
    value="Machine Learning Fundamentals"
)

if topic:
    st.write("You selected:", topic)
else:
    st.warning("Please enter a topic before asking a question.")

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear Chat
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
user_input = st.chat_input(
    "Ask me something about your topic..."
)

if user_input:

    if not topic.strip():
        st.warning("Please enter a topic first.")
        st.stop()

    # Display User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # AI Prompt
    prompt = f"""
You are an AI Learning Buddy helping a beginner student.

Selected topic:
{topic}

Student question:
{user_input}

Instructions:
- Explain the concept clearly and simply.
- Assume the student is a beginner.
- Avoid unnecessary technical jargon.
- Use bullet points when helpful.
- Include a simple real-world example when useful.
- If the question is related to programming, include a small code example when appropriate.
- If the question is outside the selected topic, politely mention that and still try to help.
"""

    # Generate AI Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(prompt)
                answer = response.text

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as e:
                st.error(
                    "Sorry, I couldn't generate a response. "
                    "Please check your API configuration and try again."
                )