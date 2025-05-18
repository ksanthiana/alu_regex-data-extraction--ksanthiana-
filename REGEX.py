# alu_regex-data-extraction-ksanthiana
# Regex Data Extractor using Python

import re

# Sample string with different types of data to extract
sample_data = """
Visit our site: https://www.example.com or https://subdomain.example.org/page.
Call us at (123) 456-7890, 123-456-7890 or 123.456.7890.
Use your credit card 1234 5678 9012 3456 or 1234-5678-9012-3456 to purchase.
The event starts at 14:30(24-hour format) and ends at 2:30 PM(12-hour format).
The price is $19.99 or $1,234.56.
"""

# Regex patterns for each data type
regex_patterns = {
    "URLs": r'https?://[^\s]+',
    "Phone Numbers": r'(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4})',
    "Credit Cards": r'\b(?:\d{4}[- ]?){3}\d{4}\b',
    "Time": r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b',
    "Currency": r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\$\d+'
}

# Extract and display matches
for title, pattern in regex_patterns.items():
    print(f"\n{title}:")
    matches = re.findall(pattern, sample_data)
    if matches:
        for match in matches:
            print(f" - {match}")
    else:
        print(" - None found.")