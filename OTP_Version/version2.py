
import smtplib
import random
from twilio.rest import Client

account_sid = 'ACf4f7f6195d9a802477e8f551eff6b45d'
auth_token = '3a8bee5b077481d4a81afa6634c2bb5a'
client = Client(account_sid, auth_token)
twilio_num = '+14706169780'
target = '+919004244603'

def generateOtp(n=6):
    otp = ""
    for i in range(n):
        otp += str(random.randint(0, 9))
    return otp

def validateMobile(mobile):
    return len(mobile) == 10 and mobile.isdigit()


def validateEmailID(receiver):
    if "@" not in receiver or "." not in receiver:
        return False
    return True

def sendOTPOverMobile(target, otp):
    if (validateMobile(target)):
        target = "+91" + target
        message = client.messages.create(
            body="Your OTP is " + otp,
            from_=twilio_num,
            to=target
        )

        print(message.body)
        print("Check Mobile Number", target)
    else:
        print("Enter valid mobile number!!")

def sendOTPOverEmail(receiver, otp):
    body = "Your OTP is " + otp

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, body)

    print("Mail sent - OTP: ", otp)


if __name__ == "__main__":

    print("Send OTP via email\n")
    sender = "rahulwankhede1981@gmail.com"
    password = "charkwwceuseemjd"
    receiver = input("Enter mail: ")
    otp = generateOtp(6)
    if (validateEmailID(receiver)):
        sendOTPOverEmail(receiver, otp)
    else:
        print("Enter your valid mail!!")

    send_twilio = input("\nWant to send OTP via SMS: ")
    if send_twilio.lower() == "yes":
        target = input("Enter mobile: ")
        sendOTPOverMobile(target, otp)
    else:
        print("\nProgram Ended\n")

