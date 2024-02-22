import config
from utils.data_processing import preprocess_data
from utils.text_generation import generate_text
from utils.visualization import visualize_data
import matplotlib.pyplot as plt
import numpy as np
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

def main():
    try:
        # Read input text from the user
        input_text = input("Enter the input text: ")
        
        # Initialize T5 model for text generation
        t5_model = T5Model()
        
        # Generate text based on the input using T5 model
        generated_text = t5_model.generate_text(input_text)
        
        # Display the generated text
        print("\nGenerated Text:")
        print(generated_text)
        
        # Save generated text to a file
        save_option = input("\nDo you want to save the generated text to a file? (yes/no): ").lower()
        if save_option == 'yes':
            filename = input("Enter the filename to save the text: ")
            with open(filename, 'w') as file:
                file.write(generated_text)
                print(f"Generated text saved to {filename}")
        
        # Visualize the generated text
        visualize_data(generated_text)
        
        # Enhance visualization with statistical analysis
        word_count = len(generated_text.split())
        unique_words = len(set(generated_text.split()))
        word_lengths = [len(word) for word in generated_text.split()]
        
        # Plot histogram of word lengths
        plt.figure(figsize=(10, 5))
        plt.hist(word_lengths, bins=np.arange(0, max(word_lengths) + 1, 1), color='skyblue', edgecolor='black', alpha=0.7)
        plt.title('Histogram of Word Lengths')
        plt.xlabel('Word Length')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
        
        # Print statistical summary
        print("\nStatistical Summary:")
        print(f"Total Words: {word_count}")
        print(f"Unique Words: {unique_words}")
        print(f"Average Word Length: {np.mean(word_lengths):.2f}")
        print(f"Maximum Word Length: {max(word_lengths)}")
        print(f"Minimum Word Length: {min(word_lengths)}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
