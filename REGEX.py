# alu_regex-data-extraction-ksanthiana
# Regex Data Extractor using Python


# Sample predefined text
sample_text = """
Visit https://www.apple.com, https://www.igihe.com or https://mail.google.com to learn more.
Call support at (123) 456-7890, 123-456-7890 or 123.456.7890.
Prices range from $19.99 to $1,234.56 and sometimes just $5.
Your card number 1234 5678 9012 3456 or 1234-5678-9012-3456 can be used.
Meeting starts at 14:30 or 2:30 PM.
"""

import re

class DataExtractor:
    def __init__(self, text):
        self.text = text

    def extract_urls(self):
        pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
        return re.findall(pattern, self.text)

    def extract_phone_numbers(self):
        pattern = r'(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4})'
        return re.findall(pattern, self.text)

    def extract_credit_cards(self):
        pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
        return re.findall(pattern, self.text)

    def extract_time(self):
        pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'
        return re.findall(pattern, self.text)

    def extract_currency(self):
        pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\$\d+'
        return re.findall(pattern, self.text)

    def display_results(self):
        print("🔍 Regex Data Extraction Results:\n")

        results = {
            "🌐 URLs": self.extract_urls(),
            "📞 Phone Numbers": self.extract_phone_numbers(),
            "💳 Credit Card Numbers": self.extract_credit_cards(),
            "⏰ Time (12h/24h)": self.extract_time(),
            "💰 Currency Amounts": self.extract_currency()
        }

        for label, matches in results.items():
            print(f"{label}:")
            if matches:
                for item in matches:
                    print(f"  ➤ {item}")
            else:
                print("  ⚠️ None found.")
            print()




# Run the extractor
extractor = DataExtractor(sample_text)
extractor.display_results()

