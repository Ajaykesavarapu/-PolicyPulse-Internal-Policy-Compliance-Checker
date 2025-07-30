import re
import json

class PolicyScanner:
    def __init__(self, rules_path='rules.json'):
        with open(rules_path, 'r') as f:
            self.rules = json.load(f)

    def scan_text(self, text):
        flagged = []
        for i, line in enumerate(text.split('\n')):
            for rule in self.rules:
                if re.search(rule['pattern'], line, re.IGNORECASE):
                    flagged.append({
                        'line_no': i+1,
                        'text': line,
                        'rule_id': rule['id'],
                        'description': rule['description']
                    })
        return flagged

# Usage:
# scanner = PolicyScanner()
# results = scanner.scan_text("Sample text with confidential info john@example.com")
