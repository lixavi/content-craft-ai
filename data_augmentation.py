# utils/data_augmentation.py

import random

def augment_data(text):
    # Randomly apply data augmentation techniques
    augmented_text = text
    
    # Randomly shuffle words
    augmented_text = shuffle_words(augmented_text)
    
    # Randomly insert noise
    augmented_text = insert_noise(augmented_text)
    
    return augmented_text

def shuffle_words(text):
    words = text.split()
    random.shuffle(words)
    return ' '.join(words)

def insert_noise(text, noise_level=0.1):
    words = text.split()
    num_noise_words = int(len(words) * noise_level)
    for _ in range(num_noise_words):
        idx = random.randint(0, len(words) - 1)
        words.insert(idx, generate_noise_word())
    return ' '.join(words)

def generate_noise_word():
    # Generate a random noise word
    noise_words = ["xyz", "abc", "123", "!!!"]
    return random.choice(noise_words)
