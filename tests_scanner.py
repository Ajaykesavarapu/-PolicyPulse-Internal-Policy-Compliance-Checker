import unittest
from scanner import PolicyScanner

class TestPolicyScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = PolicyScanner()

    def test_forbidden_keyword(self):
        text = "This is confidential"
        result = self.scanner.scan_text(text)
        self.assertTrue(any(flag['rule_id'] == 'FORBIDDEN_TERM' for flag in result))

    def test_email_detection(self):
        text = "Contact me at test@example.com"
        result = self.scanner.scan_text(text)
        self.assertTrue(any(flag['rule_id'] == 'PII_EMAIL' for flag in result))

    def test_phone_detection(self):
        text = "My number is 9876543210"
        result = self.scanner.scan_text(text)
        self.assertTrue(any(flag['rule_id'] == 'PII_PHONE' for flag in result))

    def test_no_flag(self):
        text = "This line is clean"
        result = self.scanner.scan_text(text)
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()
