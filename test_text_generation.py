# tests/test_text_generation.py

import unittest
from utils.text_generation import generate_text

class TestTextGeneration(unittest.TestCase):
    def test_generate_text(self):
        # Test generating text with default parameters
        input_text = "This is a test input."
        generated_text = generate_text(input_text)
        self.assertTrue(isinstance(generated_text, str))

    def test_generate_text_max_length(self):
        # Test generating text with maximum length constraint
        input_text = "This is a test input."
        max_length = 50
        generated_text = generate_text(input_text, max_length=max_length)
        self.assertTrue(len(generated_text) <= max_length)

    def test_generate_text_temperature(self):
        # Test generating text with different temperature values
        input_text = "This is a test input."
        temperature_low = 0.5
        temperature_high = 1.5
        generated_text_low_temp = generate_text(input_text, temperature=temperature_low)
        generated_text_high_temp = generate_text(input_text, temperature=temperature_high)
        self.assertNotEqual(generated_text_low_temp, generated_text_high_temp)

    def test_generate_text_num_return_sequences(self):
        # Test generating multiple sequences of text
        input_text = "This is a test input."
        num_return_sequences = 3
        generated_text = generate_text(input_text, num_return_sequences=num_return_sequences)
        self.assertTrue(isinstance(generated_text, list))
        self.assertEqual(len(generated_text), num_return_sequences)

if __name__ == "__main__":
    unittest.main()
