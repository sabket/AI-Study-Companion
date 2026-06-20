import streamlit as st
from google import genai
import time

# ---------------- CONFIGURATION ---------------- #

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

st.set_page_config(
    page_title="CATALYST | Smart Learning Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- UI CUSTOMIZATION ---------------- #

hide_default_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stTextInput > div > div > input {
    border-radius: 8px;
}

.stButton>button {
    width:100%;
    border-radius:8px;
}
</style>
"""

st.markdown(hide_default_style, unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("📚 CATALYST")
    st.caption("Smart Learning Assistant")

    st.divider()

    st.markdown("### Study Workspace")

    task = st.selectbox(
        "Select a Task",
        [
            "Study Plan",
            "Quiz",
            "Notes Summary",
            "Exam Preparation"
        ]
    )

    topic = st.text_input(
        "Enter Topic",
        placeholder="e.g. Thermodynamics, Calculus, Organic Chemistry"
    )

    execute_btn = st.button(
        "Generate",
        use_container_width=True
    )

    st.divider()

    st.caption(
        "Developed by Sanket Agarwal"
    )

# ---------------- MAIN PAGE ---------------- #

st.title("CATALYST")

st.subheader("Smart Learning Assistant")

st.write(
    "Helping students learn with clarity, consistency, and confidence."
)

st.divider()

st.info(
"""
Welcome!

Choose a task from the sidebar and enter a topic to get started.

Some examples:

• Calculus

• Newton's Laws

• Organic Chemistry

• Cell Biology

• World History
"""
)

# ---------------- GENERATION ---------------- #

if execute_btn:

    if topic.strip() == "":

        st.warning(
            "Please enter a topic before generating the response."
        )

    else:

        with st.status(
            "Preparing your study guide...",
            expanded=True
        ) as status:

            st.write("Analyzing topic...")
            time.sleep(0.5)

            st.write("Building response...")
            time.sleep(0.5)

            st.write("Finalizing output...")
            time.sleep(0.5)

            # ---------- PROMPTS ---------- #

            if task == "Study Plan":

                prompt = f"""
You are a helpful study mentor.

Create a practical study plan for {topic}.

Use a friendly and encouraging tone.

Include:

- Overview
- Weekly schedule
- Important concepts
- Revision tips

Focus on understanding and consistency.
"""

            elif task == "Quiz":

                prompt = f"""
Create a multiple-choice quiz on {topic}.

Include:

- 10 questions
- Four options for each question
- Correct answers with explanations

Make the questions suitable for students.
"""

            elif task == "Notes Summary":

                prompt = f"""
Create concise revision notes for {topic}.

Use headings and bullet points.

Focus on important concepts and key ideas.

Write naturally like a teacher explaining to students.
"""

            else:

                prompt = f"""
Create an exam preparation strategy for {topic}.

Include:

- Important topics
- Weekly revision schedule
- Practice recommendations
- Exam-day tips

Use a supportive and motivating tone.
"""

            try:

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                output_text = response.text

                status.update(
                    label="Study guide ready.",
                    state="complete",
                    expanded=False
                )

            except Exception as e:

                output_text = f"Error: {e}"

                status.update(
                    label="Unable to generate response.",
                    state="error",
                    expanded=False
                )

        st.subheader("📘 Your Study Guide")

        st.markdown(output_text)

# ---------------- FOOTER ---------------- #

st.divider()

st.caption(
    "CATALYST Smart Learning Assistant | Powered by Gemini"
)
