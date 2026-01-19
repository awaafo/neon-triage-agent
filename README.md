# Neon Triage Lab: AI Security Agent

### 🚀 Live Prototype
**[View the Interactive Dashboard (Lovable)](https://neon-triage-lab.lovable.app)**

## Overview
Neon Triage is an automated security operations agent designed to reduce "alert fatigue" for Level 1 SOC analysts. It utilizes Large Language Models (LLMs) to ingest unstructured server logs, parse them into structured JSON, and assign a risk score based on context.

To prevent AI hallucinations, this engine includes a deterministic **Verification Layer** that cross-references AI verdicts against a known "Allow List" of internal IP addresses.

## Project Structure
- `agent_logic.py`: Core decision engine containing the AI simulation and guardrails.
- `log_parser.py`: Regex-based utilities for cleaning and normalizing raw log data.
- `requirements.txt`: Python dependencies.

## Key Features
1.  **Noise Reduction:** Uses Regex to strip timestamps and metadata before API calls.
2.  **Structured Output:** Enforces JSON schema for downstream automation.
3.  **Hallucination Guardrails:** Overrides AI "High Risk" flags if the entity is a known safe internal actor.

## How to Run
```bash
python agent_logic.py
