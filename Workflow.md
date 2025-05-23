
---

# 🛠 Project Workflow: Food Insecurity Email Automation System

---

## ✅ 1. Setup Google Gmail Access (for SMTP + IMAP)

### 🔐 Step-by-Step to Get Gmail App Password:

1. Go to: [https://myaccount.google.com/security](https://myaccount.google.com/security)
2. Scroll down to **"2-Step Verification"** → turn it ON (if not already).
3. After enabling, scroll down to **"App Passwords"**.
4. Choose:

   * App: **Mail**
   * Device: **Other (Custom Name)** → e.g., *Email Automation*
5. Click **Generate**
6. Copy the 16-character password (e.g., `xgfh ytre lmnv asdf`)

> ✅ Use this in your `.env` or config as `EMAIL_PASSWORD`.

---

## ✅ 2. Prepare Files

### 🗂 Required Files:

* `sample.xlsx` → your master patient list (Name, Email, etc.)
* `form_responses.csv` → downloaded from Microsoft Forms (auto-named)

### ✍ Sample Format for `sample.xlsx`:

| Name     | Email                                             |
| -------- | ------------------------------------------------- |
| Ali Khan | [alikhan@gmail.com](mailto:alikhan@gmail.com)     |
| Jane Doe | [janedoe@example.com](mailto:janedoe@example.com) |

---

## ✅ 3. Microsoft Forms Setup

### 📋 Create a Follow-up Form

1. Go to: [https://forms.office.com](https://forms.office.com)
2. Create form titled **Food Support Details**
3. Add questions:

   * ZIP Code
   * Preferred Contact Method (Text / Call)
   * Household Size
   * Dietary Needs
   * Do you have access to transportation?
4. Share → anyone with link can respond → **copy link**
5. Paste link in `send_followup()` in your code

---

## ✅ 4. How to Use the Code (Workflow)

---

### 🚀 Initial Send

Run:

```python
send_emails()
```

> Sends emails to all patients in `sample.xlsx`

---

### 📨 Check Replies

Run:

```python
check_responses()
```

> Connects to Gmail, reads replies like `"yes"`/`"no"`, updates Excel, and sends follow-up form to "yes" responders.

---

### 🔄 Merge Form Responses

After users fill Microsoft Form:

1. Download Form data as `.csv`
2. Run:

```python
merge_form_responses()
```

> Merges ZIP, Contact Method, etc. into the same Excel (`sample.xlsx`)

---

### 💡 Clean the Excel (optional)

To fix extra columns or garbage rows:

```python
df = pd.read_excel("sample.xlsx")
df.dropna(how="all", inplace=True)
df = df.loc[:, ~df.columns.duplicated()]
df.to_excel("sample.xlsx", index=False)
```

---

## ✅ 5. Recap Flow (Visual)

```plaintext
[✓] sample.xlsx   -->   send_emails()
                          ↓
              [Patient receives email]

                          ↓
                Patient replies "yes"

                          ↓
            check_responses() updates status
                          ↓
          Sends MS Form link for details

                          ↓
  Download Form results → merge_form_responses()
                          ↓
     sample.xlsx now has all complete data!
```
