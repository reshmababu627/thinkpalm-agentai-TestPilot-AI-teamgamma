from ai_engine import AIEngine

class TestCaseGenerator:
    def __init__(self, ai_engine: AIEngine):
        self.ai = ai_engine
        
    def generate(self, requirements_text: str) -> str:
        prompt = f"""
You are an elite AI QA Automation Architect and Senior SDET.
Based on the following requirements, generate comprehensive manual and automation test cases.

Ensure you cover:
- Positive test cases
- Negative test cases
- Edge & Boundary value test cases
- Security and Role-based test cases

Format the output strictly as a clean Markdown table with the following columns:
| Test Case ID | Module Name | Feature Name | Test Scenario | Description | Preconditions | Priority | Severity | Test Type | Test Data | Test Steps | Expected Result | Environment | Automation Candidate (Yes/No) |

Requirements:
{requirements_text}

Only output the Markdown table and a brief introduction. Avoid lengthy explanations.
"""
        return self.ai.generate_content(prompt)
