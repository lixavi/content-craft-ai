import config
from utils.data_processing import preprocess_data
from utils.text_generation import generate_text
from utils.visualization import visualize_data
import matplotlib.pyplot as plt

def main():
    try:
        # Read input text from the user
        input_text = input("Enter the input text: ")
        
        # Preprocess the input text
        processed_text = preprocess_data(input_text)
        
        # Generate text based on the input
        generated_text = generate_text(processed_text)
        
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
        
        # Show the visualization
        plt.show()
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
