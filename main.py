import os
import requests
from PyPDF2 import PdfReader

print("hello world")

response = requests.get("https://www.supremecourt.gov/opinions/22pdf/21-86_l5gm.pdf")
pdf = open('pdf_test.pdf', 'wb')
pdf.write(response.content)
pdf.close()

reader = PdfReader('pdf_test.pdf')
pages = len(reader.pages)
page = reader.pages[10]
print(page.extract_text)

os.remove('pdf_test.pdf')

print("number of pages is", pages)
print("finished")