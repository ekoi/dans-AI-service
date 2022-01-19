import pdfplumber as pdfp
import requests
import os


def download_pdf_file(url, pdf_dir, pdf_filename):
    with requests.get(url) as r:
        if r.status_code == 200:
            with open(pdf_dir + '/' + pdf_filename, 'wb') as f:
                f.write(r.content)
            return os.path.abspath(pdf_dir + '/' + pdf_filename)
        else:
            print(pdf_filename, ' is restricted file')

    return pdf_filename


def extract_pdf_to_text(pdf_file_path):
    pdf_string = ""

    with pdfp.open(pdf_file_path) as pdf:
        for page in pdf.pages:
            print(page.extract_text())
            pdf_string += page.extract_text()

    print(pdf_string)
    return pdf_string
