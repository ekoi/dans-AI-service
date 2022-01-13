import PyPDF2


def read_PDF(pdf_file_path):
    pdf_file_obj = open(pdf_file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    pdf_num_pages = pdf_reader.numPages
    print(pdf_num_pages)

    output = []
    for i in range(pdf_num_pages):
        page = pdf_reader.getPage(i)
        output.append(page.extractText())
    print(output)

    # closing the pdf file object
    pdf_file_obj.close()
