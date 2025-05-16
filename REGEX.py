# alu_regex-data-extraction-kazeange
# Regular Expression Extraction Tool

import re

# Test input string with mixed data types
test_string = """
Contact us at user@example.com or firstname.lastname@company.co.uk.
Visit our site: https://www.example.com or https://subdomain.example.org/page.
Call us at (123) 456-7890, 123-456-7890 or 123.456.7890.
Use your credit card 1234 5678 9012 3456 or 1234-5678-9012-3456 to purchase.
The event starts at 14:30 and ends at 2:30 PM.
Here is some HTML: <p>Paragraph</p> <div class=\"example\">Example</div> <img src=\"image.jpg\" alt=\"description\">
Don't forget to use hashtags like #example or #ThisIsAHashtag.
The price is $19.99 or $1,234.56 or $100.
"""

# Dictionary of regex patterns
patterns = {
    "Emails": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+',
    "URLs": r'https?://[^\\s]+',
    "Phone Numbers": r'(\\(\\d{3}\\)\\s?\\d{3}-\\d{4}|\\d{3}[-.]\\d{3}[-.]\\d{4})',
    "Credit Cards": r'\\b(?:\\d{4}[- ]?){3}\\d{4}\\b',
    "Time": r'\\b(?:[01]?\\d|2[0-3]):[0-5]\\d(?:\\s?[APap][Mm])?\\b',
    "HTML Tags": r'<[^>]+>',
    "Hashtags": r'#\\w+',
    "Currency": r'\\$\\d{1,3}(?:,\\d{3})*(?:\\.\\d{2})?|\\$\\d+'
}

# Extract and display matches
for name, pattern in patterns.items():
    print(f"\n{name} Matches:")
    matches = re.findall(pattern, test_string)
    for match in matches:
        print(f" - {match}")
