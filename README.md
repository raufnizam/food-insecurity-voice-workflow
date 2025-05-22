
---

```markdown
# 📧 Food Insecurity Email Automation System

This project automates the process of:

1. Sending customized emails to a list of patients from an Excel file.
2. Monitoring replies via Gmail (IMAP).
3. Updating the Excel sheet based on responses to detect food insecurity.

---

## 🚀 Features

- ✅ Reads patient names & emails from Excel (`.xlsx`)
- ✅ Sends custom email messages via Gmail SMTP
- ✅ Parses email replies using IMAP
- ✅ Automatically marks `"Yes"` or `"No"` in Excel
- ✅ Console logs for every step (with [REPLY] previews)

---

## 📁 Folder Structure

```

your-project/
├── sample.xlsx                  # Input Excel file (Name, Email)
├── updated\_sample.xlsx          # Auto-saved result with Food Insecurity status
├── email\_automation.ipynb       # Main Jupyter notebook
├── README.md                    # This file

````

---

## 📦 Requirements

- Python 3.7+
- Gmail account with **App Passwords enabled**
- IMAP access enabled in Gmail settings

---

## 📄 Setup

### 1. 📌 Gmail Preparation

- Go to [Google Account > Security > App Passwords](https://myaccount.google.com/security)
- Generate an App Password for "Mail"
- Enable **IMAP access** in Gmail settings

### 2. 📦 Install Dependencies

```bash
pip install pandas openpyxl
````

> Jupyter is optional but recommended for interactive use.

---

## 🧪 Running the Project

### 📤 1. Send Emails

Use `send_emails()` function to send inquiry emails to all contacts in `sample.xlsx`.

```python
send_emails()
```

### 📥 2. Check for Responses

Use `check_responses()` to scan Gmail for replies and update the sheet accordingly.

```python
check_responses()
```

---

## 📝 Excel Format

Ensure your `sample.xlsx` looks like this:

| Name       | Email                                             |
| ---------- | ------------------------------------------------- |
| John Doe   | [johndoe@example.com](mailto:johndoe@example.com) |
| Jane Smith | [janesmith@gmail.com](mailto:janesmith@gmail.com) |

A `Food Insecurity` column will be added/updated automatically.

---

## 🛡️ Safety Tips

* Do **not** share your App Password.
* Gmail may rate-limit if too many emails are sent at once. Add `time.sleep(1)` between sends.
* Always test with your own email first before bulk sending.

---

## 📈 Example Output

```
[INFO] Excel file loaded successfully.
[📤] Sent to John Doe <johndoe@example.com>
[INFO] Connecting to IMAP...
[REPLY] janesmith@gmail.com ➜ "yes, i need help."
[✅] Marked YES for janesmith@gmail.com
[✅] Response check complete.
```



---
