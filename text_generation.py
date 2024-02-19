from models.t5_model import T5Model

def generate_text(input_text, max_length=100, temperature=0.7, num_return_sequences=1):
    t5_model = T5Model("t5-small")
    return t5_model.generate_text(input_text, max_length=max_length, temperature=temperature, num_return_sequences=num_return_sequences)
