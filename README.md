# AI-Powered Test Automation Assistant 🤖

A professional-grade AI assistant designed to accelerate software testing by generating BDD scenarios and Playwright automation scripts for the **OrangeHRM** application. Powered by **OpenRouter AI**.

## 🚀 Latest Status
- **AI Engine**: Migrated from Google Gemini to **OpenRouter AI** with `openai/gpt-4o-mini`.
- **UI Refresh**: Implemented a clean, standard interface with a **Light Blue** (`#E0F2FE`) professional background.
- **Improved Contrast**: Optimized typography for readability with dark-navy fonts on light-blue surfaces.
- **Workflow Support**: Seamless generation of Gherkin Code, Playwright Python scripts, and Coverage Gap analysis.

## ✨ Key Features
- **BDD Scenario Synthesis**: Convert feature descriptions into actionable Gherkin steps.
- **Playwright Forge**: Generate implementation-ready automation scripts using the **Page Object Model (POM)**.
- **Intelligent Coverage**: Spots testing blind spots and suggests edge cases automatically.
- **Environment Driven**: Scalable configuration via `.env` files for model and key management.

## 🛠 Project Structure
- `app.py`: The primary Streamlit dashboard logic and styling.
- `ai_engine.py`: Core logic for OpenRouter API communication.
- `gherkin_generator.py`: Prompt logic for BDD scenario creation.
- `playwright_generator.py`: Engine for script forging.
- `coverage_analyzer.py`: Automated gap detection module.

## ⚙️ Setup Instructions

### 1. Installation
```bash
pip install -r requirements.txt
playwright install
```

### 2. Configuration
Configure your `.env` file in the project root:
```env
OPENROUTER_API_KEY=your_key_here
OPENROUTER_MODEL=openai/gpt-4o-mini
HTTP_REFERER=http://localhost:8501
X_TITLE=TestAutomationAssistant
```

### 3. Execution
```bash
streamlit run app.py
```

## 🌐 Application under Test
[OrangeHRM Global Demo](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

---
Developed as part of the **Mini-Project** portfolio.
