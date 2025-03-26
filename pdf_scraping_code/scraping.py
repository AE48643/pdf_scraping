import pdfplumber

pdf_file_path = "/workspaces/pdf_scraping/pdf_file/DA SP25.pdf"

with pdfplumber.open(pdf_file_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            print(text)
        else:
            print("No text")