from multiprocessing import context
import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from python"
body = "Hi uwu Hi uwu siu"
sender_email = "argonz0102@gmail.com"
receiver_email = "norwayexprez@gmail.com"
password = input("Password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email")

with smtplib.SMTP_SSL("smtp.gmail.com", 465,context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Succes")