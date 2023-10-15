"""
Description:
This script continuously listens for voice commands using the 
microphone. When the command "capture" is detected, it takes a 
screenshot and increments the filename. The loop runs indefinitely 
until the "stop" command is heard.

Requirements:
- Install the necessary libraries using the following commands:

Libraries:
- pyautogui: Used for taking screenshots.
- SpeechRecognition: Used for transcribing audio commands.
- pyaudio: Required by SpeechRecognition for working with the microphone.

Author: Suresh Paul
Date: October 15, 2023
"""

import contextlib
import pyautogui
import speech_recognition as sr

counter = 0
output_folder = "screenshot_images"

def saveScreenshot():
    global counter
    filename = f"{output_folder}/screenshot-{str(counter)}.png"
    pyautogui.screenshot(filename)
    counter += 1
    print("Screenshot taken!")

# Create a Recognizer object
r = sr.Recognizer()

while True:
    # Start listening for audio
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = r.listen(source)

    # transcribe the audio
    with contextlib.suppress(Exception):
        text = r.recognize_google(audio)
        if "capture" in text.lower():
            saveScreenshot()
        elif "stop" in text.lower():
            break