## 📘 `alu_regex-data-extraction-ksanthiana`

A Python command-line tool to extract structured data from text using regular expressions. It can identify and extract:

* URLs
* Phone numbers
* Credit card numbers
* Time formats (12h and 24h)
* Currency values

---

### 🚀 Features

* Interactive CLI interface
* Option to use preloaded `sample_text` or your own input
* Extracts one data type at a time
* Uses Python's built-in `re` module

---

### 📂 Project Structure

```
📁 alu_regex-data-extraction-ksanthiana
├── REGEX.py        # Main script
├── README.md           # Documentation
```

---

### ✅ How to Use

1. **Run the Script**

```bash
python extractor.py
```

2. **Choose What to Extract**

You'll see this prompt:

```
What would you like to extract?
1. URLs
2. Phone Numbers
3. Credit Card Numbers
4. Time Formats
5. Currency Amounts
6. Exit
```

3. **Input the Text**

You’ll be asked:

```
Do you want to use the sample text? (yes/no):
```

Choose `yes` to use default sample, or `no` to paste your own.

---

### 🧪 Sample `sample_text`

```python
sample_text = """
Visit https://www.apple.com, https://www.igihe.com or https://mail.google.com to learn more.
You can also reach us at (123) 456-7890 or 123-456-7890.
Use your credit cards 1234-5678-9012-3456 to make a purchase.
The event starts at 14:30 and ends at 2:30 PM.
Tickets cost $19.99, $1,234.56 or even $100 for VIP access.
"""
```

---

### 🧾 Supported Patterns

| 🔢 Option | 🗂️ Data Type        | 🧪 Regex Pattern                           | 💡 Example                                |                                  |
| --------: | -------------------- | ------------------------------------------ | ----------------------------------------- | -------------------------------- |
|         1 | **URLs**             | `https?://[a-zA-Z0-9.-]+(?:/[^\s,()\]]*)?` | `https://www.apple.com`                   |                                  |
|         2 | **Phone Numbers**    | \`($\d{3}$\s?\d{3}-\d{4}                   | \d{3}\[-.]\d{3}\[-.]\d{4})\`              | `(123) 456-7890`, `123-456-7890` |
|         3 | **Credit Cards**     | `\b(?:\d{4}[- ]?){3}\d{4}\b`               | `1234-5678-9012-3456`                     |                                  |
|         4 | **Time Formats**     | \`\b(?:\[01]?\d                            | 2\[0-3]):\[0-5]\d(?:\s?\[APap]\[Mm])?\b\` | `14:30`, `2:30 PM`               |
|         5 | **Currency Amounts** | \`\$\d{1,3}(?:,\d{3})\*(?:.\d{2})?         | \$\d+\`                                   | `$19.99`, `$1,234.56`            |

---

### 💡 Example Run

```text
Enter your choice (1-6): 2
Do you want to use the sample text? (yes/no): yes

📞 Phone Numbers Found:
  ➤ (123) 456-7890
  ➤ 123-456-7890
```

---

🛠 Requirements

Python 3.x
Regular Expressions (re module)
🚀 How to Run
Clone this repository:
git clone https://github.com/ksanthiana/alu_regex-data-extraction--ksanthiana-.git



👤 Author

Kaze Ange Santhiana

ALU Student | Junior Full Stack Developer

📄 License

This project is for educational purposes at ALU. You are free to use, modify, and share it.
