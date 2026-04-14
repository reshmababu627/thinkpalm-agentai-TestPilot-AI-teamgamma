# AI-Powered Test Automation Assistant 🤖

This application helps QA engineers quickly generate BDD scenarios and Playwright test scripts for the OrangeHRM application using Google Gemini AI.

## 🚀 Getting Started

### 1. Install Dependencies
Ensure you have Python installed. Then run:
```bash
pip install -r requirements.txt
playwright install
```

### 2. Configure API Key
Create a `.env` file (one has been provided as a template) and add your Gemini API Key:
```env
GEMINI_API_KEY=your_actual_key_here
```
*Alternatively, you can enter the key directly in the UI sidebar.*

### 3. Run the Application
Start the Streamlit dashboard:
```bash
streamlit run app.py
```

## 🛠 Project Structure
- `app.py`: Streamlit User Interface.
- `ai_engine.py`: Core integration with Google Gemini Flash.
- `gherkin_generator.py`: Logic for generating Gherkin scenarios.
- `playwright_generator.py`: Logic for generating Python Playwright scripts.
- `coverage_analyzer.py`: Identifies missing scenarios and edge cases.

## 🌐 Application Under Test
[OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

## ✨ Features
- **Smart Generation**: Tailored Gherkin and Playwright code for specific OrangeHRM flows.
- **Modern UI**: Dark-themed, responsive dashboard.
- **Coverage Analysis**: Automatically spots gaps in your test strategy.
- **POM Support**: Generates code using the Page Object Model pattern.
