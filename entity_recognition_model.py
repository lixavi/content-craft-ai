# models/entity_recognition_model.py

from transformers import T5ForConditionalGeneration, T5Tokenizer
from sklearn.metrics import classification_report

class EntityRecognitionModel:
    def __init__(self, model_name="t5-small"):
        self.model_name = model_name
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(self.model_name)
        
    def train(self, train_texts, train_labels):
        # Fine-tune the model for named entity recognition
        pass
    
    def evaluate(self, eval_texts, eval_labels):
        # Evaluate the model on evaluation data
        predicted_labels = []
        for text in eval_texts:
            input_text = f"ner: {text} </s>"
            input_ids = self.tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
            outputs = self.model.generate(input_ids=input_ids, max_length=512)
            predicted_label = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            predicted_labels.append(predicted_label)
        
        report = classification_report(eval_labels, predicted_labels)
        return report
