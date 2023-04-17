import requests
from PyPDF2 import PdfReader

print("hello world")

response = requests.get("https://www.supremecourt.gov/opinions/22pdf/21-86_l5gm.pdf")
pdfContent = response.json
print(pdfContent)
reader = PdfReader(pdfContent)
# pages = len(reader.pages)

# print("number of pages is", pages)
print("finished")