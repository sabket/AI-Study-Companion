import streamlit as st

st.set_page_config(page_title="AI Study Companion")

st.title("AI Study Companion")

task = st.selectbox(
    "Choose task",
    ["Study Plan", "Quiz", "Notes Summary", "Exam Preparation"]
)

topic = st.text_input("Enter topic")

if st.button("Generate"):
    st.success(f"{task} generated for {topic}")
