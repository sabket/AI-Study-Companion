import streamlit as st
from google import genai
import time

# ---------------- CONFIGURATION ----------------

st.set_page_config(
    page_title="CATALYST",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# ---------------- STYLING ----------------

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
    padding-top:2rem;
}

div[data-testid="stSidebar"]{
    background-color:#1f2428;
}

.stButton>button{
    width:100%;
    border-radius:10px;
    height:3em;
}

.stTextInput input{
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("📚 CATALYST")
    st.caption("Smart Learning Assistant")

    st.divider()

    st.subheader("Study Workspace")

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
        placeholder="Anything that you ever wanted to learn."
    )

    generate = st.button("Generate")

    st.divider()

    st.caption("Developed by Sanket Agarwal")
    

# ---------------- MAIN PAGE ----------------

st.title("CATALYST")
st.subheader("Smart Learning Assistant")

st.write(
    "Using the technology in the best way possible."
)

st.divider()

# Welcome section

if not generate:

    st.info(
        """
Welcome! Adios Amigos!!

Choose a task from the sidebar and enter a topic to get started.
"""
    )

# ---------------- PROMPTS ----------------

if generate:

    if topic.strip() == "":
        st.warning("Please enter a topic.")
        st.stop()

    with st.status("Generating response...", expanded=True) as status:

        st.write("Understanding your request...")
        time.sleep(0.5)

        st.write("Preparing study resources...")
        time.sleep(0.5)

        st.write("Generating output...")
        time.sleep(0.5)

        if task == "Study Plan":

            prompt = f"""
You are an experienced teacher at a tuition centre.

Create a practical and friendly study plan for {topic}.

Requirements:

- Use simple language.
- Encourage the student.
- Divide into sections.
- Include weekly goals.
- Include tips and common mistakes.
- Avoid robotic language.
- Make it feel like advice from a good teacher.
"""

        elif task == "Quiz":

            prompt = f"""
Create a quiz on {topic}.

Requirements:

- 10 questions.
- Multiple choice format.
- Four options each.
- Mention correct answers.
- Give short explanations.
"""

        elif task == "Notes Summary":

            prompt = f"""
Summarize {topic}.

Requirements:

- Important points only.
- Use headings.
- Use bullet points.
- Keep it easy to revise.
"""

        else:

            prompt = f"""
Create a complete exam preparation strategy for {topic}.

Include:

- Daily routine.
- Revision timetable.
- Practice strategy.
- Common mistakes.
- Last week revision tips.

Use a motivating and friendly tone.
"""

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            output = response.text

            status.update(
                label="Study guide ready.",
                state="complete",
                expanded=False
            )

        except Exception as e:

            output = f"Error:\n\n{e}"

            status.update(
                label="Something went wrong.",
                state="error"
            )

    # ---------------- OUTPUT ----------------

    st.subheader("📘 Your Study Guide")

    if task == "Study Plan":
        st.success(
            f"Here's a study plan for **{topic}**. Feel free to adjust it according to your schedule."
        )

    elif task == "Quiz":
        st.success(
            f"Practice questions prepared for **{topic}**."
        )

    elif task == "Notes Summary":
        st.success(
            f"Quick revision notes for **{topic}**."
        )

    else:
        st.success(
            f"Exam preparation strategy prepared for **{topic}**."
        )

    st.markdown(output)

    st.divider()

    st.caption(
        "CATALYST • Driving change , delivering results."
    )
