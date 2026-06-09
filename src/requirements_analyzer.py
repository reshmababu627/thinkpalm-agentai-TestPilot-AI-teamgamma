from ai_engine import AIEngine

class RequirementsAnalyzer:
    def __init__(self, ai_engine: AIEngine):
        self.ai = ai_engine
        
    def analyze(self, requirements_text: str) -> str:
        prompt = f"""
You are an elite AI QA Automation Architect and Requirement Analysis Expert.
Perform a deep analysis of the following software requirements and generate a comprehensive response containing exactly these sections:

1. Requirement Summary
2. Identified Modules
3. Functional Flows
4. Test Scenarios
5. Automation Feasibility
6. Risks and Assumptions

Requirements:
{requirements_text}

Format the output cleanly in Markdown, using headers, bullet points, and tables where appropriate. Make it look professional and enterprise-grade.
"""
        return self.ai.generate_content(prompt)
