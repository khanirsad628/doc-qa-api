from transformers import MarianMTModel,MarianTokenizer
from app.enums.docconstants import Models

class Translate:
    def __init__(self,model_dwd:bool=True):
        self.model_dwd = model_dwd
        self.model_name = Models.HELSENKI_MODEL.value
        if self.model_dwd:
            self.dwd_model()

    def dwd_model(self):
        if self.model_dwd:
            self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
            self.model = MarianMTModel.from_pretrained(self.model_name)

    def translate_english(self,extrated_list:list[dict]):
        if not hasattr(self,"model") or not hasattr(self,"tokenizer"):
            raise Exception("Model not loaded. Need to Load Model First")
        for texts in extrated_list:
            text_list = texts["text"].split("\n")
            line_list = []
            for text in text_list:
                tokens = self.tokenizer.prepare_seq2seq_batch(text,return_tensors="pt")
                translated = self.model.generate(**tokens)
                english = self.tokenizer.decode(translated[0],skip_special_tokens=True)
                line_list.append({"urdu":text,"English":english})
            texts["Translate"] = line_list
        return extrated_list

