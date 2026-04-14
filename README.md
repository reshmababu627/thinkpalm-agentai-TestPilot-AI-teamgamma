# AI-Powered Test Automation Assistant 🤖

A professional-grade AI assistant designed to accelerate software testing by generating BDD scenarios and Playwright automation scripts for the **OrangeHRM** application. Powered by **OpenRouter AI**.

## 🚀 Recent Updates
- **AI Engine**: Migrated from Google Gemini to **OpenRouter AI** for enhanced flexibility and multi-model support.
- **Model**: Now using `openai/gpt-4o-mini` for high-speed, cost-effective test synthesis.
- **Enlarged Branding**: Increased the visibility of the primary dashboard title for a bolder, more professional look.
- **Light Blue UI**: Refreshed the interface with a soft light blue theme (`#E0F2FE`) and high-contrast dark text.
- **Config**: Integrated `.env` for secure credential management.

## ✨ Key Features
- **BDD Scenario Generation**: Effortlessly create structured given/when/then scenarios for complex business flows.
- **Playwright Automation**: Instantly generate Python Playwright scripts using the **Page Object Model (POM)** pattern.
- **Coverage Analysis**: Automatically identifies missing edge cases and validation checks in your test coverage.
- **Feature Placeholders**: Guided input area with real-world testing examples.

## 🛠 Project Structure
- `app.py`: The main Streamlit dashboard.
- `ai_engine.py`: Centralized OpenRouter AI integration logic.
- `gherkin_generator.py`: Specialized BDD synthesis module.
- `playwright_generator.py`: Logic-based automation script generation.
- `coverage_analyzer.py`: Intelligent test gap analysis.

## ⚙️ Setup Instructions

### 1. Installation
```bash
pip install -r requirements.txt
playwright install
```

### 2. Configuration
Create a `.env` file in the root directory and add your OpenRouter credentials:
```env
OPENROUTER_API_KEY=your_actual_key_here
OPENROUTER_MODEL=openai/gpt-4o-mini
HTTP_REFERER=http://localhost:8501
X_TITLE=TestAutomationAssistant
```

### 3. Run the Application
```bash
streamlit run app.py
```

## 🌐 Application Under Test
[OrangeHRM Demo Portal](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

---
Developed as part of the **Mini-Project** portfolio.
