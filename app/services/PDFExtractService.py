import pdfplumber

class PDFExtract:
    def __init__(self,file_list):
        self.file_list = file_list
    
    def extract_text(self):
        for file in self.file_list:
            extracted = []
            print(file)
            with pdfplumber.open(file) as pdf:
                for i , page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if text:
                         data = {"page":i,"text":text}
                         extracted.append(data)
        return extracted 