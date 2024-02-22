# models/summarization_model.py

from transformers import T5ForConditionalGeneration, T5Tokenizer
from sklearn.metrics import rouge_score

class SummarizationModel:
    def __init__(self, model_name="t5-small"):
        self.model_name = model_name
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(self.model_name)
        
    def train(self, train_texts, train_summaries):
        # Fine-tune the model for text summarization
        pass
    
    def evaluate(self, eval_texts, eval_summaries):
        # Evaluate the model on evaluation data
        predicted_summaries = []
        for text in eval_texts:
            input_text = f"summarize: {text} </s>"
            input_ids = self.tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
            summary_ids = self.model.generate(input_ids=input_ids, max_length=150, min_length=30, length_penalty=2.0, num_beams=4)
            summarized_text = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            predicted_summaries.append(summarized_text)
        
        rouge_scores = rouge_score.rouge_n(eval_summaries, predicted_summaries)
        return rouge_scores
