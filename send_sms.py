"""
Twilio Speech-Activated Messaging

This Python script uses Twilio API to send a predefined 
message with an image to a list of phone numbers when a 
specific phrase ("vatican cameos") is detected in the 
audio input from the user.

Requirements:
- pip install twilio
- pip install SpeechRecognition
- pip install python-dotenv

Author: Suresh Paul
Date: October 15, 2023
"""

import os
import time
import speech_recognition as sr
from list import contact_list
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
from_number = os.environ.get("FROM_NUMBER")

from_number = f"+{from_number}"
print(from_number)

contacts = contact_list()

# Collect all phones/emails into a list and check for duplicates
all_phones = [phone for phone, email in contacts.values()]
unique_phones = list(set(all_phones))
# print(f"phone number list = {unique_phones}")

all_emails = [email for phone, email in contacts.values()]
unique_emails = list(set(all_emails))
# print(f"email list = {unique_emails}")

client = Client(account_sid, auth_token)

# Create a Recognizer object
r = sr.Recognizer()

def send_message(to_number,from_number):
    message = client.messages.create(
        from_=from_number,
        body="!!! Have a nice day! See you next week !!!",
        media_url="https://png.pngtree.com/png-clipart/20230609/original/pngtree-thank-you-text-decorated-by-floral-ornaments-picture-image_8538603.png",
        to=to_number
    )
    return message.sid

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = r.listen(source)
    return audio

def main():
    
    # Start listening for audio
    audio = listen_for_command()

    # Transcribe the audio
    try:
        text = r.recognize_google(audio)
        if "christmas" in text.lower():
            for number in unique_phones:
                print(send_message(from_number=from_number,to_number=number))
                print(f"message sent to = {number}")
                time.sleep(1)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()