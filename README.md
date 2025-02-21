# Twilio SMS Notification System


##FOR PDFS DIFF CODE BELOW CHECK


# 📩 Twilio SMS Notification System with PDF Storage

This project allows storing **PDF health report links** in a database and automatically sending them via **Twilio SMS**.

---

## 💂️ Project Directory Structure
```
twilio_sms_project/
│—— app.py               # Flask API to store and send SMS
│—— send_sms.py          # Function to send SMS
│—— config.py            # Twilio credentials & database config
│—— database.py          # Database connection & operations
│—— requirements.txt     # Dependencies
│—— README.md            # Documentation
│—— health_reports.db    # SQLite database (auto-created)
```

---

## 🚀 Getting Started

### **1️⃣ Install Required Packages**
```sh
pip install twilio flask sqlite3
```

---

## 🔑 Configuration

### **2️⃣ `config.py` (Twilio & Database Config)**
Create a `config.py` file and add your Twilio credentials:

```python
# Twilio Credentials (Replace with your own)
TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"

# Receiver Phone Number (for testing)
RECEIVER_PHONE_NUMBER = "recipient_phone_number"

# Database Configuration
DATABASE_NAME = "health_reports.db"
```
📌 **Note:** The recipient number must be verified if you’re using a free Twilio account.

---

## 🛄️ Database Handling

### **3️⃣ `database.py` (Handle Database)**
```python
import sqlite3
from config import DATABASE_NAME

def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pdf_url TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

def save_pdf_url(pdf_url):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO reports (pdf_url) VALUES (?)", (pdf_url,))
    conn.commit()
    conn.close()

def get_latest_pdf():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT pdf_url FROM reports ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    
    conn.close()
    return row[0] if row else None

# Create table on first run
create_table()
```

---

## 📀 Sending an SMS

### **4️⃣ `send_sms.py` (Send SMS with Stored PDF Link)**
```python
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, RECEIVER_PHONE_NUMBER
from database import get_latest_pdf

def send_sms():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    pdf_url = get_latest_pdf()
    if not pdf_url:
        print("No PDF found in the database!")
        return
    
    message = client.messages.create(
        body=f"Your health report is ready. Download it here: {pdf_url}",
        from_=TWILIO_PHONE_NUMBER,
        to=RECEIVER_PHONE_NUMBER
    )

    print(f"SMS sent successfully! Message SID: {message.sid}")

# Run the function
send_sms()
```

---

## 🌐 Flask API for PDF Upload

### **5️⃣ `app.py` (Flask API to Store PDF URL & Send SMS)**
```python
from flask import Flask, request, jsonify
from database import save_pdf_url
from send_sms import send_sms

app = Flask(__name__)

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    data = request.json
    pdf_url = data.get("pdf_url")

    if not pdf_url:
        return jsonify({"error": "PDF URL is required"}), 400

    save_pdf_url(pdf_url)
    send_sms()  # Automatically send SMS after saving

    return jsonify({"message": "PDF saved and SMS sent successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 📓 Dependencies

### **6️⃣ `requirements.txt`**
```txt
flask
twilio
sqlite3
```

---

## 🎮 How to Use

### **Step 1: Start Flask API**
```sh
python app.py
```
It will run on **http://127.0.0.1:5000/**

### **Step 2: Store PDF URL**
Use **Postman** or run this command in the terminal:
```sh
curl -X POST http://127.0.0.1:5000/upload_pdf -H "Content-Type: application/json" -d '{"pdf_url": "https://example.com/health_report.pdf"}'
```
💪 **This saves the PDF link in the database and sends an SMS.**

### **Step 3: Check Your SMS**
You should receive:
```txt
Your health report is ready. Download it here: https://example.com/health_report.pdf
```

---

## 🚀 Summary
✔ Stores PDF URL in SQLite  
✔ Retrieves latest PDF URL  
✔ Sends SMS via Twilio  

🚀 **Let me know if you need any modifications!** 🚀



