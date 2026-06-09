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
from document_parser import DocumentParser
from requirements_analyzer import RequirementsAnalyzer
from testcase_generator import TestCaseGenerator
from export_utils import ExportUtils
import tempfile
import os

# Page configuration
st.set_page_config(
    page_title="TestPilotAI - Test Automation Dashboard",
    page_icon="🤖",
    layout="wide",
)

# Custom UI CSS for Screenshot-matching Design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    /* Main background */
    .stApp {
        background-color: #F8FAFC;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #1E3A8A;
        color: white;
    }

    .stSidebar [data-testid="stMarkdownContainer"] p {
        color: white !important;
    }
    
    .sidebar-menu-item {
        display: flex;
        align-items: center;
        padding: 12px 20px;
        margin: 4px 0;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s;
        color: #CBD5E1;
        text-decoration: none;
    }

    .sidebar-menu-item:hover {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
    }

    .sidebar-active {
        background-color: rgba(255, 255, 255, 0.15);
        color: white !important;
        font-weight: 600;
    }

    /* Top Bar Styling */
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0;
        margin-bottom: 30px;
    }

    .search-container {
        position: relative;
        background: white;
        border-radius: 12px;
        padding: 8px 16px;
        display: flex;
        align-items: center;
        width: 300px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        border: 1px solid #E2E8F0;
    }

    /* Dashboard Header */
    .dashboard-title {
        color: #0F172A;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
    }

    .dashboard-project {
        color: #64748B;
        font-size: 1rem;
        margin-top: 4px;
        margin-bottom: 32px;
    }

    /* Card Styling */
    .dashboard-card {
        background-color: white;
        border-radius: 20px;
        padding: 32px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        border: 1px solid #F1F5F9;
        margin-bottom: 32px;
    }

    .card-title {
        color: #0F172A;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .card-subtitle {
        color: #64748B;
        font-size: 0.95rem;
        margin-bottom: 24px;
    }

    /* Output Sections */
    .output-header {
        padding: 12px 16px;
        border-radius: 12px 12px 0 0;
        color: #1E3A8A;
        background-color: #EFF6FF;
        font-weight: 600;
        font-size: 1rem;
        border-bottom: 1px solid #DBEAFE;
    }
    
    /* Visual metrics */
    .metric-bar {
        height: 10px;
        border-radius: 5px;
        width: 100%;
        margin-top: 8px;
    }

    .heatmap-bar { background: linear-gradient(to right, #3B82F6, #8B5CF6, #10B981, #F59E0B); }
    .req-bar { background: linear-gradient(to right, #F87171 20%, #FBBF24 50%, #34D399 100%); }

    /* Fix Streamlit spacing */
    [data-testid="column"] {
        padding: 0 15px !important;
    }

    .stTextArea textarea {
        background-color: #F8FAFC !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 12px !important;
    }

    /* Hide default elements */
    #MainMenu {visibility: hidden;}
    
    /* Spacer utility */
    .section-spacer {
        height: 24px;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Sidebar Redesign
    with st.sidebar:
        st.markdown("""
            <div style='margin-bottom: 2rem;'>
                <h2 style='color: white; display: flex; align-items: center; gap: 12px;'>
                    <span style='background: white; color: #1E3A8A; padding: 4px 8px; border-radius: 8px;'>✈️</span> 
                    TestPilotAI
                </h2>
            </div>
            
            <div class="sidebar-menu-item sidebar-active">🏠 Dashboard</div>
            <br>
        """, unsafe_allow_html=True)
        
        st.markdown("<p style='color: #94A3B8; font-size: 0.8rem; margin-bottom: 4px; padding-left: 10px;'>SELECT MODULE</p>", unsafe_allow_html=True)
        flow_option = st.selectbox(
            "Select Targeted Flow",
            ["Login flow", "Users", "Job Title", "Pay grades"],
            index=0,
            label_visibility="collapsed"
        )
        
        st.markdown(f"""
            <div style='position: fixed; bottom: 20px; left: 20px; display: flex; align-items: center; gap: 10px; color: white;'>
                <img src="https://ui-avatars.com/api/?name=User+Profile&background=random" style='width: 32px; border-radius: 50%;'>
                <span>User Profile</span>
            </div>
        """, unsafe_allow_html=True)

    # Top Bar & Header
    st.markdown("""
        <div class="top-bar">
            <div class="search-container">
                <span style="color: #94A3B8; margin-right: 8px;">🔍</span>
                <input type="text" placeholder="Search" style="border: none; outline: none; width: 100%; background: transparent;">
            </div>
            <div style="display: flex; gap: 16px; align-items: center;">
                <span style="font-size: 1.2rem; cursor: pointer;">🔔</span>
                <img src="https://ui-avatars.com/api/?name=Admin&background=0284c7&color=fff" style='width: 36px; border-radius: 50%; border: 2px solid white; box-shadow: 0 2px 4px rgba(0,0,0,0.1); cursor: pointer;'>
            </div>
        </div>
        <h1 class="dashboard-title">Test Automation Dashboard</h1>
        <p class="dashboard-project">Project: OrangeHRM Web App</p>
    """, unsafe_allow_html=True)

    # Initialization
    api_key = os.getenv("OPENROUTER_API_KEY", "")
    engine = AIEngine(api_key=api_key)
    req_analyzer = RequirementsAnalyzer(engine)
    tc_gen = TestCaseGenerator(engine)
    playwright_gen = PlaywrightGenerator(engine)
    coverage_anl = CoverageAnalyzer(engine)

    if 'requirements_text' not in st.session_state: st.session_state.requirements_text = ""
    if 'analysis_result' not in st.session_state: st.session_state.analysis_result = ""
    if 'testcases_result' not in st.session_state: st.session_state.testcases_result = ""
    if 'playwright_result' not in st.session_state: st.session_state.playwright_result = ""
    if 'coverage_result' not in st.session_state: st.session_state.coverage_result = ""
    if 'is_processing' not in st.session_state: st.session_state.is_processing = False
    if 'current_action' not in st.session_state: st.session_state.current_action = None

    # Input Section with File Upload
    st.markdown("""
        <div class="dashboard-card">
            <h3 class="card-title">Requirement Input</h3>
            <p class="card-subtitle">Upload requirement document or enter text manually</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        uploaded_file = st.file_uploader("Upload Requirement Document (PDF, DOCX, TXT)", type=['pdf', 'docx', 'txt'])
        if uploaded_file is not None:
            # Save temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp:
                tmp.write(uploaded_file.getvalue())
                tmp_path = tmp.name
            try:
                st.session_state.requirements_text = DocumentParser.parse(tmp_path)
                st.success("Document parsed successfully!")
            except Exception as e:
                st.error(f"Error parsing document: {e}")
            finally:
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)

    with col2:
        feature_desc = st.text_area(
            "Or Describe Scenario/Requirement Manually",
            value=st.session_state.requirements_text[:1000] if st.session_state.requirements_text else "",
            placeholder="As a user, I want to...",
            height=150
        )
        if feature_desc and feature_desc != (st.session_state.requirements_text[:1000] if st.session_state.requirements_text else ""):
            st.session_state.requirements_text = feature_desc

    st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

    # Actions Row
    btn_col1, btn_col2, btn_col3, btn_col4 = st.columns(4)
    is_disabled = st.session_state.is_processing or not st.session_state.requirements_text

    if btn_col1.button("📊 Analyze Requirements", disabled=is_disabled, use_container_width=True):
        st.session_state.current_action = "analyze"; st.session_state.is_processing = True; st.rerun()
    if btn_col2.button("📋 Generate Test Cases", disabled=is_disabled, use_container_width=True):
        st.session_state.current_action = "testcases"; st.session_state.is_processing = True; st.rerun()
    if btn_col3.button("🤖 Playwright Scripts", disabled=is_disabled, use_container_width=True):
        st.session_state.current_action = "script"; st.session_state.is_processing = True; st.rerun()
    if btn_col4.button("🔍 Analyze Coverage", disabled=is_disabled, use_container_width=True):
        st.session_state.current_action = "coverage"; st.session_state.is_processing = True; st.rerun()

    st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

    # Processing Logic
    if st.session_state.is_processing and st.session_state.current_action:
        with st.spinner("Processing with AI Engine..."):
            try:
                if st.session_state.current_action == "analyze":
                    st.session_state.analysis_result = req_analyzer.analyze(st.session_state.requirements_text)
                elif st.session_state.current_action == "testcases":
                    st.session_state.testcases_result = tc_gen.generate(st.session_state.requirements_text)
                elif st.session_state.current_action == "script":
                    # Hardcoded flow integration based on selection
                    st.session_state.playwright_result = playwright_gen.generate(st.session_state.requirements_text, flow_option)
                elif st.session_state.current_action == "coverage":
                    st.session_state.coverage_result = coverage_anl.analyze(st.session_state.requirements_text, "Generated from requirements", flow_option)
            except Exception as e:
                st.error(f"Error: {e}")
            finally:
                st.session_state.is_processing = False
                st.session_state.current_action = None
                st.rerun()

    # Output Section Tabs
    st.markdown("""
        <div class="dashboard-card" style="padding: 24px;">
            <h3 class="card-title">Output Dashboard</h3>
        </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Requirement Analysis", "Test Cases", "Automation Scripts", "Coverage", "Export Hub"])

    with tab1:
        if st.session_state.analysis_result:
            st.markdown(st.session_state.analysis_result)
        else:
            st.info("No analysis generated yet.")

    with tab2:
        if st.session_state.testcases_result:
            st.markdown(st.session_state.testcases_result)
        else:
            st.info("No test cases generated yet.")

    with tab3:
        if st.session_state.playwright_result:
            st.code(st.session_state.playwright_result, language="python")
        else:
            st.info("No automation script generated yet.")

    with tab4:
        if st.session_state.coverage_result:
            st.markdown(st.session_state.coverage_result)
        else:
            st.info("No coverage analysis generated yet.")

    with tab5:
        st.markdown("### Export Artifacts")
        if st.session_state.playwright_result:
            zip_data = ExportUtils.create_framework_zip({f"test_{flow_option.replace(' ','_').lower()}.py": st.session_state.playwright_result})
            st.download_button("📦 Download Playwright Framework (ZIP)", data=zip_data, file_name="playwright_framework.zip", mime="application/zip")
            
        if st.session_state.testcases_result:
            csv_data = ExportUtils.export_test_cases_csv(st.session_state.testcases_result)
            if csv_data:
                st.download_button("📊 Download Test Cases (CSV)", data=csv_data, file_name="test_cases.csv", mime="text/csv")

if __name__ == "__main__":
    main()
