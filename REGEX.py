# alu_regex-data-extraction-ksanthiana
# Regex Data Extractor using Python


import re

# Updated sample text

sample_text = """
Visit https://www.apple.com, https://www.igihe.com or https://mail.google.com to learn more.
You can also reach us at (123) 456-7890 or 123-456-7890.
Use your credit cards 1234-5678-9012-3456  to make a purchase.
The event starts at 14:30 and ends at 2:30 PM.
Tickets cost $19.99, $1,234.56 or even $100 for VIP access.
"""

class DataExtractor:
    def __init__(self, text):
        self.text = text

    def extract_urls(self):
        pattern = r'https?://[a-zA-Z0-9.-]+(?:/[^\s,()\]]*)?'
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

    def extract_by_choice(self, choice):
        if choice == "1":
            return "🌐 URLs", self.extract_urls()
        elif choice == "2":
            return "📞 Phone Numbers", self.extract_phone_numbers()
        elif choice == "3":
            return "💳 Credit Card Numbers", self.extract_credit_cards()
        elif choice == "4":
            return "⏰ Times", self.extract_time()
        elif choice == "5":
            return "💰 Currency Amounts", self.extract_currency()
        else:
            return None, None

if __name__ == "__main__":
    print("🔍 Welcome to the Regex Data Extractor!")

    while True:
        print("\n What would you like to extract?")
        print("1. URLs")
        print("2. Phone Numbers")
        print("3. Credit Card Numbers")
        print("4. Time Formats")
        print("5. Currency Amounts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "6":
            print("👋 Goodbye! Thanks for using the Regex Data Extractor.")
            break

        label = {
            "1": "🌐 URLs",
            "2": "📞 Phone Numbers",
            "3": "💳 Credit Card Numbers",
            "4": "⏰ Times",
            "5": "💰 Currency Amounts"
        }.get(choice, None)

        if label:
            print(f"\nYou chose to extract: {label}")
            use_sample = input("Do you want to use the sample text? (yes/no): ").strip().lower()

            if use_sample == "yes":
                text = sample_text
            else:
                text = input("\n📝 Enter the text to extract from:\n")

            extractor = DataExtractor(text)
            results = extractor.extract_by_choice(choice)

            print(f"\n{label} Found:")
            if results:
                for item in results:
                    print(f"  ➤ {item}")
            else:
                print("  ⚠️ None found.")
        else:
            print("❌ Invalid choice. Please choose a number between 1 and 6.")

