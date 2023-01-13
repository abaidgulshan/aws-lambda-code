import boto3, json, os
from datetime import date
from datetime import timedelta 
import smtplib  
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def lambda_handler(event,context):
    
# Replace sender@example.com with your "From" address. 
    # This address must be verified.
    SENDER = 'new@example.com'  # no-reply@example.com SES verified domain or email ID
    SENDERNAME = 'Abaid SES TEST with Credentials' # YourFirstName YourLastName
    
    RECIPIENT  = "abaid.gulshan@gmail.com" # Your Email ID
    
    # Replace smtp_username with your Amazon SES SMTP user name.
    USERNAME_SMTP = "XXXXXXXXXXX"  # SES username 
    
    # Replace smtp_password with your Amazon SES SMTP password.
    PASSWORD_SMTP = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    HOST = "email-smtp.us-east-1.amazonaws.com"
    PORT = 587

    ses_payload = "test"

    # The subject line of the email.
    SUBJECT = 'TEST SES EMAIL WITH SMTP credentails'
    
    BODY_HTML = ses_payload
    
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
    msg['To'] = (', ').join(RECIPIENT.split(','))

    # Try to send the message.
    try:  
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.send_message(msg)
        server.close()
    # Display an error message if something goes wrong.
    except Exception as e:
        print ("Error: ", e)
    else:
        print ("Email sent!")