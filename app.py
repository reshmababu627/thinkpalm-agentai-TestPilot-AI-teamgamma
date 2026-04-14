import streamlit as st
import os
import requests
from dotenv import load_dotenv

# Load environment variables early
load_dotenv()

from ai_engine import AIEngine
from gherkin_generator import GherkinGenerator
from playwright_generator import PlaywrightGenerator
from coverage_analyzer import CoverageAnalyzer

# Page configuration
st.set_page_config(
    page_title="AI Test Automation Assistant",
    page_icon="🧪",
    layout="wide",
)

# Custom UI CSS
st.markdown("""
<style>
    .stApp {
        background-color: #E0F2FE;
        color: #0F172A;
    }
    label, p, span, h1, h2, h3 {
        color: #0F172A !important;
    }
    .stButton>button {
        background-color: #2563EB;
        color: white;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("AI Test Automation Assistant")
    st.write("Generate professional Gherkin scenarios and Playwright scripts effortlessly.")

    # Sidebar
    with st.sidebar:
        st.header("Configuration")
        api_key = os.getenv("OPENROUTER_API_KEY", "")
        
        if not api_key:
            st.error("Missing OpenRouter Key in .env")
        else:
            st.success("API Key Loaded Successfully")
            
        st.divider()
        st.info("🌐 **Target:** OrangeHRM Demo")
        
        flow_option = st.selectbox(
            "Select Targeted Flow",
            ["Login Flow", "User Management Flow", "Job Titles Flow", "Pay Grades Flow"],
            index=0
        )

    # Initialize Engine
    engine = AIEngine(api_key=api_key)
    gherkin_gen = GherkinGenerator(engine)
    playwright_gen = PlaywrightGenerator(engine)
    coverage_anl = CoverageAnalyzer(engine)

    # Main Area
    st.subheader("Feature Description")
    
    placeholder_example = "Example: Admin should be able to add a new Job Title with a name and description. Validate that the Job Title is saved and appears correctly in the list."
    
    feature_desc = st.text_area(
        "Enter flow or requirement details below:",
        placeholder=placeholder_example,
        height=200
    )

    col1, col2, _ = st.columns([1, 1, 2])
    generate_gherkin = col1.button("Generate Gherkin Scenarios")
    generate_script = col2.button("Generate Playwright Script")

    # State management
    if 'gherkin_result' not in st.session_state:
        st.session_state.gherkin_result = ""
    if 'playwright_result' not in st.session_state:
        st.session_state.playwright_result = ""
    if 'coverage_result' not in st.session_state:
        st.session_state.coverage_result = ""

    # Actions
    if generate_gherkin:
        if not api_key:
            st.error("Please provide an API key in the .env file.")
        else:
            with st.spinner("Synthesizing Gherkin..."):
                st.session_state.gherkin_result = gherkin_gen.generate(feature_desc, flow_option)
                st.session_state.coverage_result = coverage_anl.analyze(feature_desc, st.session_state.gherkin_result, flow_option)

    if generate_script:
        if not api_key:
            st.error("Please provide an API key in the .env file.")
        elif not st.session_state.gherkin_result:
            with st.spinner("Generating dependencies first..."):
                st.session_state.gherkin_result = gherkin_gen.generate(feature_desc, flow_option)
                st.session_state.playwright_result = playwright_gen.generate(st.session_state.gherkin_result, flow_option)
                st.session_state.coverage_result = coverage_anl.analyze(feature_desc, st.session_state.gherkin_result, flow_option)
        else:
            with st.spinner("Forging Playwright script..."):
                st.session_state.playwright_result = playwright_gen.generate(st.session_state.gherkin_result, flow_option)

    # Output Showcase
    st.divider()
    if st.session_state.gherkin_result or st.session_state.playwright_result:
        tabs = st.tabs(["📄 Gherkin Code", "🐍 Playwright Python", "📊 Coverage Analysis"])

        with tabs[0]:
            if st.session_state.gherkin_result:
                st.code(st.session_state.gherkin_result, language="gherkin")

        with tabs[1]:
            if st.session_state.playwright_result:
                st.code(st.session_state.playwright_result, language="python")

        with tabs[2]:
            if st.session_state.coverage_result:
                st.markdown(st.session_state.coverage_result)

if __name__ == "__main__":
    main()
