# models/translation_model.py

from transformers import T5ForConditionalGeneration, T5Tokenizer

class TranslationModel:
    def __init__(self, model_name="t5-small"):
        self.model_name = model_name
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(self.model_name)
        
    def translate_text(self, text, source_lang="en", target_lang="fr"):
        # Format input as T5 model input
        input_text = f"translate {source_lang} to {target_lang}: {text} </s>"
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
        
        # Generate translated output
        translated_ids = self.model.generate(input_ids=input_ids, max_length=512)
        translated_text = self.tokenizer.decode(translated_ids[0], skip_special_tokens=True)
        
        return translated_text
