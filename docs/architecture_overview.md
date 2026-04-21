# 🏗️ TestPilotAI: Architecture Overview

## Introduction
**TestPilotAI** is an agentic AI system designed to automate the transition from software requirements to executable automation scripts. By leveraging a multi-agent orchestration pattern, the system ensures that each phase of the testing lifecycle—analysis, design, and implementation—is handled by a specialized AI persona.

## Multi-Agent Workflow
The system operates as a sequential pipeline:

1.  **Requirement Analyzer**: Processes raw natural language input to identify key entities and business logic.
2.  **BDD Generator Agent**: Transforms the analyzed requirements into structured Gherkin scenarios (Feature, Background, Scenario, Examples).
3.  **Automation Engineer Agent**: Converts BDD steps into production-ready Playwright Python scripts using the Page Object Model (POM) pattern.
4.  **Quality Auditor Agent**: Analyzes the generated suite against the original requirements to identify coverage gaps and security risks.

## Tech Stack
- **Frontend**: Streamlit (Reactive Python Dashboard)
- **Engine**: OpenRouter/Groq API (Large Language Models)
- **Automation**: Playwright (Synchronous Python API)
- **State management**: Streamlit Session State for orchestration persistence.

## Design Philosophy
The core philosophy of TestPilotAI is **Contextual Specialization**. Instead of using a single generic prompt, the system breaks the problem into sub-tasks, providing each agent with the specific context (selectors, POM patterns, BDD best practices) required to produce high-fidelity output.
