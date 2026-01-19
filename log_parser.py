import re

class LogParser:
    def __init__(self):
        # Regex to capture the timestamp and the actual message body separately
        self.log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (.*)')

    def clean_log(self, raw_log: str) -> str:
        """
        Strips timestamps and brackets to reduce token usage 
        before sending to the LLM.
        """
        match = self.log_pattern.search(raw_log)
        if match:
            # Return only the message part (Group 2)
            return match.group(2).strip()
        return raw_log

    def extract_ip(self, text: str):
        """Helper to extract IP addresses from text using Regex."""
        ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
        match = ip_pattern.search(text)
        return match.group(0) if match else None
