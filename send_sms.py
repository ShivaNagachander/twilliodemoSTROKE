from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, RECEIVER_PHONE_NUMBER

def send_sms():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body="Hello! This is a test SMS from Twilio.",
        from_=TWILIO_PHONE_NUMBER,
        to=RECEIVER_PHONE_NUMBER
    )

    print(f"SMS sent successfully! Message SID: {message.sid}")

# Run the function
send_sms()
