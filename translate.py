from app.services.PDFExtractService import PDFExtract
from app.enums.docconstants import DocConstants
from app.services.TresnlatorService import Translate
import os 

UPLOAD_DIR = os.path.join(os.path.abspath(os.getcwd()),'doc-qa-api',DocConstants.UPLOAD_DIR.value)

files = os.listdir(UPLOAD_DIR)
file_list = [UPLOAD_DIR+"\\"+f for f in files if f.endswith(".pdf")]
print(file_list)
obj = PDFExtract(file_list)
extracted_list = obj.extract_text()
translate = Translate()
translated_list = translate.translate_english(extrated_list=extracted_list)
print(translated_list)