# Twilio SMS Notification System

This project allows sending SMS notifications via **Twilio**, including links to health report PDFs.  
The system stores PDF links in a database and automatically sends them via SMS.

---

## 📂 Project Structure
```plaintext
twilio_sms_project/
│── config.py             # Configuration file (API keys & verified recipient number)
│── send_sms.py           # Sends SMS with Twilio
│── requirements.txt      # Python dependencies
│── README.md             # Documentation (this file)
🚀 Getting Started
1️⃣ Clone the Repository

git clone https://github.com/yourusername/twilio_sms_project.git
cd twilio_sms_project
2️⃣ Create a Virtual Environment (Optional)

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies

pip install -r requirements.txt
🔑 Configuration
1️⃣ Set Up config.py
Create a config.py file and add your Twilio credentials:


import os

TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"
RECEIVER_PHONE_NUMBER = "your_verified_twilio_recipient_number"
📌 Note: The recipient number must be verified if you’re using a free Twilio account.

📡 Sending an SMS

python send_sms.py
It will fetch the latest PDF link from the database and send an SMS.
