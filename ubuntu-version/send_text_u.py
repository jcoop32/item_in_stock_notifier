import smtplib
import yaml
from email.mime import text

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com",
}


conf = yaml.full_load(open("/home/ubuntu/item_in_stock_notifier/login_details.yml"))


EMAIL1 = conf["gmail_creds1"]["email"]
PASSWORD1 = conf["gmail_creds1"]["password"]

EMAIL2 = conf["gmail_creds2"]["email"]
PASSWORD2 = conf["gmail_creds2"]["password"]


def send_message(phone_number, phone_number2, carrier, msg):
    recipient = phone_number + CARRIERS[carrier], phone_number2 + CARRIERS[carrier]
    auth = (EMAIL2, PASSWORD2)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
    message = text.MIMEText(msg)
    try:
        server.sendmail(auth[0], recipient, message.as_string())
        print("Message Sent")
    except Exception as e:
        print(e)


def send_message_one(phone_number, carrier, msg):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL2, PASSWORD2)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
    message = text.MIMEText(msg)
    try:
        server.sendmail(auth[0], recipient, message.as_string())
        print("Message Sent")
    except Exception as e:
        print(e)
