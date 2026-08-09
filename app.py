import streamlit as st

st.title("🎓 AI Learning Buddy")
st.write("An AI-powered learning assistant for interactive learning.")

topic = st.text_input(
    "📚 Enter a topic",
    "Machine Learning Fundamentals"
)

st.write("You selected:", topic)

user_input = st.chat_input("💬 Ask something about your topic...")

if user_input:
    st.write("You asked:", user_input)
