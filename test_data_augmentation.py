# tests/test_data_augmentation.py

import unittest
from utils.data_augmentation import augment_data

class TestDataAugmentation(unittest.TestCase):
    def test_augment_data(self):
        # Test augmenting data
        original_text = "This is a test sentence."
        augmented_text = augment_data(original_text)
        self.assertNotEqual(original_text, augmented_text)

    def test_shuffle_words(self):
        # Test shuffling words in text
        text = "This is a test sentence."
        shuffled_text = shuffle_words(text)
        self.assertNotEqual(text, shuffled_text)
        self.assertEqual(set(text.split()), set(shuffled_text.split()))

    def test_insert_noise(self):
        # Test inserting noise into text
        text = "This is a test sentence."
        noise_level = 0.1
        noisy_text = insert_noise(text, noise_level=noise_level)
        self.assertNotEqual(text, noisy_text)
        self.assertGreater(len(noisy_text), len(text))

    def test_generate_noise_word(self):
        # Test generating noise word
        noise_word = generate_noise_word()
        self.assertTrue(isinstance(noise_word, str))
        self.assertGreater(len(noise_word), 0)

if __name__ == "__main__":
    unittest.main()
