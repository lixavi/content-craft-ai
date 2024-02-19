import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

class T5Model:
    def __init__(self, model_name="t5-small"):
        self.model_name = model_name
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(self.model_name).to(self.device)
        
    def generate_text(self, input_text, max_length=100):
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt").to(self.device)
        output = self.model.generate(input_ids, max_length=max_length)
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text
