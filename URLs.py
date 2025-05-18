# alu_regex-data-extraction-ksanthiana
# Regex Data Extractor using Python

import re

# Sample string with different types of data to extract

text = """
Visit our site: https://www.apple.com,https://mail.google.com or https://subdomain.example.org/page.
"""

# Regex patterns for each data type

regex_patterns = {
    "URLs": r'https?://[a-zA-Z0-9.-]+(?:/[^\s,()]*)?'
}

# Extract and display matches
for title, pattern in regex_patterns.items():
    print(f"\n{title}:")
    matches = re.findall(pattern, text)
    if matches:
        for match in matches:
            print(f" - {match}")
    else:
        print(" - None found.")