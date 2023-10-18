import random
from twilio.rest import Client
import smtplib

account_sid = 'ACf4f7f6195d9a802477e8f551eff6b45d'
auth_token = '4c31b59806e2ef719a24d46ffebbfdbe'

twilio_number = '+14706169780'
target_number = '+919004244603'

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_via_sms(phone_number, otp):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Your OTP is: {otp}",
        from_=twilio_number,
        to=phone_number
    )
    print("OTP sent successfully.")

def send_otp_via_email(emailid,otp):
    server=smtplib.SMTP('smtp.gmail.com',587)


if __name__ == "__main__":
    otp = generate_otp()
    send_otp_via_sms(target_number, otp)
