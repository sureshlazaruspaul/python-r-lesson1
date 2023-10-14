"""
Converts a PDF file to individual PNG images, one per page.

Args:
 pdf_path (str): The file path of the PDF to convert.
 output_folder (str): The folder to write the PNG images.

Returns:
 None

Requirements:
pip install pymupdf
pip install pillow
"""

import fitz
from PIL import Image

# This function converts a PDF file into individual
# PNG image files, one image per page.

def pdf_to_images(pdf_path, output_folder):
    try:
        # Open the PDF file using fitz.open()
        pdf_document = fitz.open(pdf_path)

        # Iterate through each page in the PDF
        for page_number in range(pdf_document.page_count):
            try:
                # Get the page
                page = pdf_document[page_number]

                # Convert the current page to a pixmap
                pixmap = page.get_pixmap()

                # Create an image file name 
                # (you can adjust the format as needed, e.g., 'image{}.png')
                image_file_name = f"{output_folder}/page{page_number + 1}.png"

                try:
                    # Convert the pixmap to a PIL Image and save it
                    image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
                    image.save(image_file_name, format="PNG")

                except Exception as save_error:
                    print(f"Error saving page {page_number + 1} as image: {save_error}")

            except Exception as page_error:
                print(f"Error processing page {page_number + 1}: {page_error}")

    except Exception as pdf_error:
        print(f"Error opening PDF file: {pdf_error}")

    finally:
        # Close the PDF document in a finally block to ensure it gets closed even if an exception occurs
        if 'pdf_document' in locals():
            pdf_document.close()

# USAGE:
# pdf_path = "file.pdf"
# output_folder = "output_images"
# pdf_to_images(pdf_path, output_folder)