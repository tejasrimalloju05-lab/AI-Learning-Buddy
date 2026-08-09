import streamlit as st

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓"
)

st.title("🎓 AI Learning Buddy")
st.write("An AI-powered learning assistant for interactive learning.")

topic = st.text_input(
    "📚 Enter a topic",
    "Machine Learning Fundamentals"
)

st.write("You selected:", topic)

user_input = st.chat_input("Ask me something about your topic...")

if user_input:
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(
        f"Your question is about **{topic}**: {user_input}"
    )
