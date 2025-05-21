
---

In the meantime, here is your complete, polished **`README.md`** for the **Food Insecurity Notification Automation** project using **Twilio + Flask + Jupyter Notebook**.

---

```markdown
# 📞 Food Insecurity Notification Automation (Twilio + Flask + Jupyter)

This project automates **outreach calls to patients** to assess food insecurity using the **Twilio Voice API**. It calls each patient, asks them two key food access questions, and routes follow-up actions based on their input.

---

## 🚀 Features

- 🧠 Asks two automated voice questions related to food insecurity
- ⌨ Accepts keypad (DTMF) input from the user (1 = Yes, 2 = No)
- 📞 Places outbound calls using Twilio's programmable voice
- 🖥️ Flask web server handles Twilio webhook routes and logic
- 📊 Designed for integration with Excel/CSV patient data
- 🌐 Supports local development via **Ngrok**

---

## 🗂️ Project Structure

```

twilio\_food\_insecurity/
├── food\_insecurity\_voice\_workflow\.ipynb  # Jupyter Notebook for initiating calls
├── twilio\_voice\_server.py                # Flask server for Twilio webhook handling
├── sample1.xlsx                          # Excel file with patient data
├── requirements.txt                      # Dependencies

````

---

## 🧪 Setup Instructions

### 1. Clone the Repo & Set Up Environment
```bash
git clone <your-repo-url>
cd twilio_food_insecurity
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
````

### 2. Add Twilio Credentials

In your Jupyter Notebook or `.env`:

```python
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = '+1XXXXXXXXXX'
```

---

## 📞 Call Flow (Voice Logic)

1. Patient receives a call

2. First Question:

   > "Have you worried your food would run out before you had money to buy more?"

   * Press `1` for Yes
   * Press `2` for No

3. Second Question (if Yes to Q1):

   > "Did the food you bought not last, and you didn’t have money to get more?"

4. If any answer is `1`, Twilio will say:

   > "We’ll now follow up with more questions via SMS or a care team member."

5. All responses are logged in the console (for now)

---

## 🔧 Running the Project

### Step 1: Start Flask Server

```bash
python twilio_voice_server.py
```

### Step 2: Expose Flask with Ngrok

```bash
ngrok http 5000
```

Copy the HTTPS forwarding URL (e.g., `https://abcd.ngrok.io`)

### Step 3: Update Twilio Webhook

* Go to [Twilio Console > Phone Numbers](https://console.twilio.com/)
* Under “A CALL COMES IN”, choose:

  * Method: `POST`
  * URL: `https://abcd.ngrok.io/voice`
  * Save

### Step 4: Run Jupyter Notebook

Open `food_insecurity_voice_workflow.ipynb`, then:

* Load Excel data
* Set `voice_url` to your Ngrok `/voice` URL
* Run the notebook to place outbound calls

---

## 🛠️ Troubleshooting

* **Call connects but no voice?**

  * Make sure Flask is running and POST requests are hitting `/voice`
  * Confirm `Ngrok` is correctly exposing port `5000`

* **Twilio trial errors?**

  * Trial accounts can only call verified numbers
  * Upgrade to remove this restriction

* **Timeout or silence?**

  * Increase `timeout` in `Gather` block to 10–15 seconds
  * Ensure fallback `Say` is in place if no DTMF is pressed

---
