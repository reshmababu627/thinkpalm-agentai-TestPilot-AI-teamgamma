
# 🚀 TestPilotAI
### *Next-Gen AI-Powered Test Automation Dashboard*


**TestPilotAI** is a high-fidelity, multi-agent AI system designed to revolutionize the software testing lifecycle. By orchestrating specialized **Agentic AI** nodes, it transforms plain-text requirements into structured BDD scenarios, production-ready Playwright scripts, and comprehensive coverage gap analyses—all within a premium, modern dashboard.

Built for the modern QA engineer, **TestPilotAI** simplifies the bridge between requirement gathering and automation execution with state-of-the-art aesthetics and collaborative AI intelligence.

![TestPilotAI Dashboard](./docs/screenshots/dashboard.png)

---

## 📖 Project Overview
The traditional path from requirement to automated test is often fragmented and time-consuming. **TestPilotAI** orchestrates a pipeline of specialized agents—Requirement Analyzer, BDD Generator, Automation Engineer, and Quality Auditor—to automate this workflow.

---

## 🎯 Problem Statement
Manual testing is time-consuming and requires significant effort. Converting requirements into test cases and automation scripts is repetitive, error-prone, and often leads to inconsistencies and coverage gaps.

**TestPilotAI** addresses this problem by automating the entire process using AI—enabling faster, more accurate, and efficient test generation.

---

## 👥 Team Members & Contributions

### 👩‍💻 Amritha Panicker
- Collaborated with the team to define project requirements and goals  
- Designed and refined prompts for Antigravity  
- Iterated prompts multiple times to align with expected outputs  
- Tested generated results for accuracy and quality  
- Suggested improvements for functionality and UI enhancements  

---

### 👩‍💻 Reshma Babuji
- Generated the application using Antigravity based on finalized prompts  
- Verified application functionality through testing  
- Implemented iterative improvements based on feedback  
- Enhanced UI for better usability and user experience  
- Structured project folders and organized codebase  
- Prepared README documentation, screenshots, and demo setup  

---
## 🧰 Tech Stack

### 🔹 Core Technologies
- Python 3.9+  
- Streamlit 1.56.0 (Frontend Dashboard)  
- Playwright 1.58.0 (Test Automation)  

### 🔹 AI & API Integration
- OpenRouter API (LLM Gateway)  
- OpenAI SDK 2.31.0  
- Google Generative AI 0.8.3  

### 🔹 Backend & Frameworks
- FastAPI 0.135.3  
- Uvicorn 0.42.0  

### 🔹 Data & Utilities
- Pandas 3.0.2  
- NumPy 2.4.4  
- Requests 2.33.1  
- Python-dotenv 1.2.2  

### 🔹 Testing
- Pytest 9.0.3  
- Pytest-Playwright 0.7.2  

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository
git clone <repository_url>  
cd mini-project  

### 2️⃣ Install Dependencies  
Ensure you have Python 3.9+ installed:  
pip install -r requirements.txt  
playwright install  

### 3️⃣ Configure Environment Variables  
Create a `.env` file in the root directory:

OPENROUTER_API_KEY=your_key_here  
OPENROUTER_MODEL=openai/gpt-4o-mini  
HTTP_REFERER=http://localhost:8501  
X_TITLE=TestPilotAI  

### 4️⃣ Run the Application  
streamlit run src/app.py  

### 5️⃣ Access the Application  
Open your browser and go to:  
http://localhost:8501  

---

## 📸 Screenshots

### 📝 Requirement Input & Test Generation
![Requirement Input](./Screenshots/requirement_input.png)

### 📄 Gherkin Scenario Output
![Gherkin Output](./Screenshots/gherkin_output.png)

### 🖥️ Frontend Dashboard
![Frontend](./Screenshots/dashboard.png)

### 🧪 Playwright Script Output
![Playwright Script](./Screenshots/playwright_output.png)

### 🔍 Coverage Analysis
![Coverage Analysis](./Screenshots/coverage_output.png)

---

## 🎥 Demo Video

Watch the 5-minute demo here:  
👉 <your-video-link>

---

**Key Capabilities:**
- **🧠 Intelligent Interpretation**: Parses high-level feature text to extract core testing logic.
- **📄 BDD Orchestration**: Drafts comprehensive Gherkin scenarios covering happy paths, negative flows, and edge cases.
- **🐍 Automation Engineering**: Generates robust, Page Object Model (POM) compliant Playwright Python scripts.
- **🔍 Quality Audit**: Identifies coverage gaps and missing validation checks using advanced visual metrics.

---

## 🏎️ Premium Dashboard Features

The application features a state-of-the-art UI/UX designed to feel alive and responsive:

*   **⚡ Modern Workspace**: A clean, card-based interface built with the Inter font and a sleek #F8FAFC professional palette.
*   **📂 Multi-Module Sidebar**: Integrated navigation with context-aware selection for specific application flows.
*   **📊 Visual Metrics**: Real-time Heatmap and Requirements Coverage bars to visualize the depth of the generated test suite.
*   **🏗️ Grid-Based Output**: A three-column layout designed for side-by-side comparison of Gherkin, Python scripts, and Audit results.
*   **🔔 Interactive UI**: Top-bar navigation with search, notifications, and profile components for a full-application feel.
*   **🎯 Targeted Context**: Pre-optimized for the **OrangeHRM** ecosystem, providing high-precision selectors and flow logic.

### 📍 Supported Application Flows
The system is specialized for the following **OrangeHRM** modules:
- 🔐 **Login Flow**: Comprehensive authentication and session management.
- 👥 **User Management**: Creating, editing, and deleting system users.
- 💼 **Job Titles**: Configuration and validation of organizational roles.
- 💳 **Pay Grades**: Financial structures and currency mapping.

---

## 🏗️ Multi-Agent Architecture

The system operates as a sophisticated pipeline where specialized agents collaborate:

1.  **Requirement Analyzer**: Interprets raw requirement text and extracts core testing logic.
2.  **BDD Generator Agent**: (`src/gherkin_generator.py`) Architected to draft comprehensive Gherkin scenarios.
3.  **Automation Agent**: (`src/playwright_generator.py`) A specialized coding agent that transforms BDD steps into robust Playwright Python scripts.
4.  **Coverage Analyzer Agent**: (`src/coverage_analyzer.py`) Performs a "Quality Audit" to identify missing validation checks.
5.  **LLM Orchestrator**: (`src/ai_engine.py`) Manages stateful communication with the OpenRouter/Groq API.

---


## 📂 Project Structure
```text
mini-project/
├── src/                    # Source Code
│   ├── app.py              # Premium Dashboard & Orchestration
│   ├── ai_engine.py        # Backend logic & LLM connection
│   ├── gherkin_generator.py # BDD agent logic
│   ├── playwright_generator.py # Automation agent logic
│   └── coverage_analyzer.py # Audit agent logic
├── docs/
│   └── screenshots/        # UI Visuals & Dashboards
├── .env                    # Environment Secrets
├── requirements.txt        # Python Dependencies
└── README.md               # Project Documentation
```

---

### ⭐ Final Note
This project demonstrates the power of **Agentic AI**—where autonomous agents collaborate to solve complex, high-value engineering challenges with speed, precision, and a premium user experience.
