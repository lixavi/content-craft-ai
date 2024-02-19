import config
from utils.data_processing import preprocess_data
from utils.text_generation import generate_text
from utils.visualization import visualize_data

def main():
    # Read input text from the user
    input_text = input("Enter the input text: ")
    
    # Preprocess the input text
    processed_text = preprocess_data(input_text)
    
    # Generate text based on the input
    generated_text = generate_text(processed_text)
    
    # Display the generated text
    print("\nGenerated Text:")
    print(generated_text)
    
    # Visualize the generated text
    visualize_data(generated_text)

if __name__ == "__main__":
    main()
