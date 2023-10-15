"""
Email Script

This script sends personalized messages to a list of recipients using a Gmail account.
It retrieves a list of unique email addresses from a contact list, and then sends the
same message to each recipient. The script uses the smtplib library for sending emails,
dotenv for loading email credentials from a .env file, and a custom 'contact_list' module
to get recipient information.

Libraries required:
- pip install smtplib
- pip install python-dotenv

Author: Suresh Paul
Date: October 15, 2023
"""

# Required Libraries
import smtplib
import os
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from list import contact_list

# Load environment variables from a .env file
load_dotenv()

def get_unique_emails():
    """Get a list of unique email addresses from the contact list."""
    contacts = contact_list()
    all_emails = {email for _, email in contacts.values()}
    return list(set(all_emails))

def send_email(email_user, email_password, recipient, subject, message):
    """Send an email."""
    try:
        # Create SMTP connection object
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            # Start TLS encryption on connection
            server.starttls()
            # Login to SMTP server with email and password
            server.login(email_user, email_password)
            # Create and configure the email message
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            # Send email
            server.sendmail(email_user, recipient, msg.as_string())
    except Exception as e:
        print(f"Error sending email to {recipient}: {e}")

def main():
    # Sender's email credentials
    email_user = os.environ.get("EMAIL_USER")
    email_password = os.environ.get("EMAIL_PASSWORD")
    # Get unique recipient emails
    unique_emails = get_unique_emails()
    # Date
    now = datetime.now()
    date_str = now.strftime("%m/%d/%Y, %H:%M:%S")
    # Email subject
    subject = f"Today's message {date_str}: using python code"
    # Message
    message = "HI! This is me. Me is good. Complex code."
    # Send email to each recipient
    for recipient in unique_emails:
        send_email(email_user, email_password, recipient, subject, message)
        print(f"email sent to: {recipient}")

if __name__ == "__main__":
    main()