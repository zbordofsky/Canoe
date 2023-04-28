import os
import requests
import pdfplumber

def handlePdf(pdf):
    print('Starting function')
    for page in pdf.pages:
        text = page.extract_text()
        # print(text)
        print(len(text))
    print('Function done')

response = requests.get("https://www.supremecourt.gov/opinions/22pdf/21-86_l5gm.pdf")
pdf = open('pdf_test.pdf', 'wb')
pdf.write(response.content)
pdf.close()

with pdfplumber.open('pdf_test.pdf') as pdf_test:
    handlePdf(pdf_test)

os.remove('pdf_test.pdf')
print("finished")