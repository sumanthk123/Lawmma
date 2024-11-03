
import os
from pypdf import PdfReader

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    number_of_pages = len(reader.pages)
    text = ""
    for i in range(number_of_pages):
        page = reader.pages[i]
        text += page.extract_text()
    return text

upload_dir = './uploads'
for filename in os.listdir(upload_dir):
    if filename.endswith('.pdf'):
        file_path = os.path.join(upload_dir, filename)
        pdf_text = extract_text_from_pdf(file_path)
        print(f"Text from {filename}:\n{pdf_text}\n")
