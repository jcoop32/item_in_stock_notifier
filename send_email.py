from email.message import EmailMessage
import smtplib
import yaml

conf = yaml.full_load(
    open("/Users/joshcooper/item_in_stock_notifier/login_details.yml")
)

sender_email = conf["email_creds"]["email"]
sender_email_password = conf["email_creds"]["password"]


def send_email(receiver_email):
    # Create the email message
    email_message = EmailMessage()
    email_message["From"] = "coopbonusbot@outlook.com"
    email_message["To"] = receiver_email
    email_message["Subject"] = "Canon G7 X Mark II Stock Status"
    # email_message.add_attachment(f"Go to {url_to_site}")
    # Attach the message body
    # add image to email
    with open("./sc_canon.png", "rb") as img:
        img_data = img.read()
    email_message.add_attachment(img_data, maintype="image", subtype="png")
    # Connect to the SMTP server
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        # Log in to the email account
        server.starttls()  # Use if your server requires a secure connection
        server.login("coopbonusbot@outlook.com", "GiveMeMyMoney6!")
        # Send the email
        server.sendmail(
            "coopbonusbot@outlook.com", receiver_email, email_message.as_string()
        )


# send_email("coopj3265@gmail.com")
