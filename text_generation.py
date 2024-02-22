from models.t5_model import T5Model
import numpy as np
import torch
from transformers import pipeline

def generate_text(input_text, max_length=100, temperature=0.7, num_return_sequences=1):
    t5_model = T5Model("t5-small")
    return t5_model.generate_text(input_text, max_length=max_length, temperature=temperature, num_return_sequences=num_return_sequences)

def analyze_sentiment(text):
    sentiment_analyzer = pipeline("sentiment-analysis")
    result = sentiment_analyzer(text)
    return result

def main():
    try:
        # Read input text from the user
        input_text = input("Enter the input text: ")
        
        # Generate text based on the input using T5 model
        generated_text = generate_text(input_text)
        
        # Display the generated text
        print("\nGenerated Text:")
        print(generated_text)
        
        # Analyze sentiment of the generated text
        sentiment_result = analyze_sentiment(generated_text)
        print("\nSentiment Analysis:")
        for entry in sentiment_result:
            print(f"{entry['label']}: {entry['score']}")
        
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
