import streamlit as st

st.title("🎓 AI Learning Buddy")
st.write("My Streamlit app is working!")

topic = st.text_input(
    "📚 Enter a topic",
    "Machine Learning Fundamentals"
)

st.write("You selected:", topic)
