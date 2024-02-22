# utils/summarization.py

from transformers import T5ForConditionalGeneration, T5Tokenizer

class SummarizationModel:
    def __init__(self, model_name="t5-small"):
        self.model_name = model_name
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(self.model_name)
        
    def summarize_text(self, input_text, max_length=150):
        # Format input as T5 model input
        input_text = f"summarize: {input_text} </s>"
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
        
        # Generate summary output
        summary_ids = self.model.generate(input_ids=input_ids, max_length=max_length, min_length=30, length_penalty=2.0, num_beams=4)
        summarized_text = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        return summarized_text
