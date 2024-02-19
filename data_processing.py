import re
import string

def preprocess_data(data):
    # Remove special characters and punctuation
    data = remove_special_characters(data)
    
    # Lowercase the text
    data = data.lower()
    
    # Tokenize the text
    tokens = data.split()
    
    # Remove stopwords
    tokens = remove_stopwords(tokens)
    
    # Join tokens back into a string
    processed_data = ' '.join(tokens)
    
    return processed_data

def remove_special_characters(text):
    # Define pattern for special characters and punctuation
    pattern = r'[{}]'.format(re.escape(string.punctuation))
    # Remove special characters and punctuation
    text = re.sub(pattern, '', text)
    return text

def remove_stopwords(tokens):
    stopwords = ["the", "and", "is", "in", "it", "to", "a"]  # Example list of stopwords
    filtered_tokens = [token for token in tokens if token not in stopwords]
    return filtered_tokens
