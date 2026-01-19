---

#### **File 2: `agent_logic.py`**
*This is the file you referenced in your essay. It shows the Logic/Guardrails.*

```python
import json
from log_parser import LogParser

# CONFIGURATION: Known Safe Internal IPs (The "Allow List")
# In production, this would fetch from a database or IAM system.
INTERNAL_SAFE_IPS = ["192.168.1.5", "10.0.0.55", "127.0.0.1"]

class TriageAgent:
    def __init__(self):
        self.parser = LogParser()

    def verify_guardrails(self, ai_risk_score: str, ip_address: str) -> str:
        """
        The Verification Loop (Guardrail).
        Overrides the AI decision if the IP is known to be safe.
        This prevents 'hallucinations' where the AI flags internal admin traffic as malicious.
        """
        if ip_address in INTERNAL_SAFE_IPS:
            print(f"[GUARDRAIL ACTIVATED] Overriding AI verdict. {ip_address} is a known Safe Internal IP.")
            return "LOW"
        
        return ai_risk_score

    def analyze_log(self, raw_log_line: str):
        """
        Main orchestration flow:
        1. Clean Data -> 2. AI Analysis -> 3. Guardrail Check -> 4. Final Verdict
        """
        # Step 1: Clean the data
        clean_msg = self.parser.clean_log(raw_log_line)
        print(f"Processing: {clean_msg}...")

        # Step 2: Simulate AI Analysis (Mocking the LLM API call)
        # In a real app, this would be: response = openai.ChatCompletion.create(...)
        mock_ai_response = {
            "risk": "HIGH", 
            "ip": "192.168.1.5", 
            "reason": "Repeated failed login attempts detected."
        }
        
        # Step 3: Apply Guardrails
        final_risk = self.verify_guardrails(mock_ai_response['risk'], mock_ai_response['ip'])

        # Step 4: Return Structured JSON
        result = {
            "original_log": raw_log_line,
            "normalized_msg": clean_msg,
            "ai_initial_verdict": mock_ai_response['risk'],
            "final_risk_score": final_risk,
            "action_required": final_risk == "HIGH"
        }
        return json.dumps(result, indent=2)

if __name__ == "__main__":
    # Test Run
    agent = TriageAgent()
    sample_log = "2026-01-18 14:02:11 [AUTH_FAIL] Failed password for root from 192.168.1.5 port 22 ssh2"
    
    print("\n--- Starting Analysis ---")
    print(agent.analyze_log(sample_log))
    print("--- Analysis Complete ---\n")
