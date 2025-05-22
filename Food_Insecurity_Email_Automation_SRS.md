
# 📄 Software Requirements Specification (SRS)
## Project: Food Insecurity Email Notification Automation

---

### 1. Introduction

#### 1.1 Purpose
The purpose of this system is to automate email-based communication with patients identified as potentially food insecure. It will analyze responses in an Excel dataset and automatically send personalized follow-up emails to patients marked as "Yes" in the FOOD INSECURITY column.

#### 1.2 Scope
The system reads patient data from an Excel file, identifies patients flagged for food insecurity, and sends them customized email messages using Gmail’s SMTP server.

---

### 2. Functional Requirements

- The system shall read an Excel file with patient data.
- The system shall identify patients where "FOOD INSECURITY" == "Yes".
- The system shall send emails to those patients.
- The system shall log each successful or failed email.

---



### 3. System Features

#### 3.1 Email Sending
- Uses `smtplib` and Gmail SMTP server.
- Sends emails with subject and body templates.

#### 3.2 Patient Filtering
- Reads from Excel (.xlsx) file.
- Filters rows with "Yes" in the "FOOD INSECURITY" column.

---

### 4. Technologies

- Python 3.7+
- pandas
- openpyxl
- smtplib (standard lib)
- Gmail SMTP

---

### 5. Assumptions

- Users will use their Gmail account and configure an App Password.
- Email addresses and flags are correctly stored in the Excel file.

---

