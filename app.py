import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(
    page_title="AI Study Companion",
    page_icon="📚"
)

st.title("AI Study Companion")

st.write(
    "An AI assistant designed to help students with study planning, quizzes, note summaries, and exam preparation."
)

st.divider()

task = st.selectbox(
    "Select a task",
    [
        "Study Plan",
        "Quiz",
        "Notes Summary",
        "Exam Preparation"
    ]
)

topic = st.text_input(
    "Enter a topic",
    placeholder="Example: Calculus"
)

if st.button("Generate"):

    if topic == "":
        st.warning("Please enter a topic.")
    else:

        if task == "Study Plan":
            prompt = f"""
            Create a study plan for {topic}.
            Make it clear and easy to follow.
            """

        elif task == "Quiz":
            prompt = f"""
            Create a multiple-choice quiz on {topic}.
            Include answers.
            """

        elif task == "Notes Summary":
            prompt = f"""
            Summarize important notes about {topic}.
            Use bullet points.
            """

        else:
            prompt = f"""
            Create an exam preparation strategy for {topic}.
            """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        st.subheader("Result")
        st.write(response.text)

st.divider()

st.caption("Built by Sanket Agrawal")
