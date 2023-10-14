"""_summary_
This code essentially reads a PDF file, extracts its text content, 
converts it to speech, saves it as an audio file, and plays the 
audio file, all while handling potential errors during the process.
"""

# Import required modules
import pyttsx3
import PyPDF2
import os

try:
    # Create PDF reader object
    # open the PDF file in binary read mode

    pdf = PyPDF2.PdfReader(open("file.pdf", "rb"))

    # Set output file name
    outfile = "file.mp3"
    # outfile = "file.wav"

    # Initialize text-to-speech engine
    speaker = pyttsx3.init()

    clean_text = ""

    # Loop through pages
    for page_num in range(len(pdf.pages)):
        # Extract text from page
        text = pdf.pages[page_num].extract_text()

        # Clean text by removing newline chars & append
        clean_text = clean_text + text.strip().replace("\n", " ")

    # Print cleaned text
    print(clean_text)

    # Save audio file
    speaker.save_to_file(clean_text, outfile)

    # execute the text-to-speech conversion and wait for it to finish
    speaker.runAndWait()

    # stop the text-to-speech engine
    speaker.stop()

    # play file
    os.startfile(outfile)

except FileNotFoundError:
    print("Error: The 'file.pdf' file was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")