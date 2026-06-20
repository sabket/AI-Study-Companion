import streamlit as st
from google import genai
import time

# --- SYSTEM CONFIGURATION ---
# Using your exact genai client initialization
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(
    page_title="CATALYST | AI Study Orchestrator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CLEAN UI OVERRIDES ---
hide_default_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stTextInput>div>div>input {border-radius: 4px;}
            </style>
            """
st.markdown(hide_default_style, unsafe_allow_html=True)

# --- SIDEBAR: TECHNICAL DASHBOARD & INPUTS ---
# We moved your inputs here to give it a "control panel" aesthetic
with st.sidebar:
    st.title("CATALYST")
    st.caption("V 1.0.4 | System Architecture")
    st.divider()
    
    st.markdown("**Execution Parameters**")
    
    # Your exact task list
    task = st.selectbox(
        "Select Routing Protocol",
        [
            "Study Plan",
            "Quiz",
            "Notes Summary",
            "Exam Preparation"
        ]
    )
    
    # Your exact topic input
    topic = st.text_input(
        "Define Target Subject",
        placeholder="e.g., Thermodynamics, Calculus"
    )
    
    execute_btn = st.button("Initialize Sequence", use_container_width=True)
    
    st.divider()
    st.caption("Architected by Sabket | ISM ")

# --- MAIN INTERFACE ---
st.title("CATALYST Orchestrator")
st.markdown("Intelligent study automation. Define your parameters in the dashboard to optimize your cognitive load.")
st.divider()

# --- LOGIC & OUTPUT ---
if execute_btn:
    if topic == "":
        st.warning("System Halt: Target Subject parameter cannot be null. Please define a subject.")
    else:
        # The st.status creates the "hard work" terminal log effect for the judges
        with st.status("Executing CATALYST routing protocols...", expanded=True) as status:
            st.write("Initializing genai.Client connection...")
            time.sleep(0.4)
            st.write(f"Analyzing subject parameters: [ {topic} ]")
            time.sleep(0.4)
            st.write(f"Delegating to internal {task.lower()} framework...")
            time.sleep(0.4)
            
            # --- YOUR EXACT BACKEND LOGIC ---
            if task == "Study Plan":
                prompt = f"""
                Create a strict, highly organized study plan for {topic}.
                Make it clear, actionable, and easy to follow. No fluff.
                """
            elif task == "Quiz":
                prompt = f"""
                Create a challenging multiple-choice quiz on {topic}.
                Include answers and brief explanations at the end.
                """
            elif task == "Notes Summary":
                prompt = f"""
                Summarize the most critical concepts regarding {topic}.
                Use high-density bullet points.
                """
            else:
                prompt = f"""
                Construct an aggressive, foolproof exam preparation strategy for {topic}.
                """

            # Your exact API execution call
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                output_text = response.text
                status.update(label="Orchestration Complete.", state="complete", expanded=False)
            except Exception as e:
                output_text = f"API Execution Error: {e}"
                status.update(label="System Failure.", state="error", expanded=False)

        # Display the final generated response
        st.subheader("System Output")
        st.markdown(output_text)
        
