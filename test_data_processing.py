# tests/test_data_processing.py

import unittest
from utils.data_processing import preprocess_data, remove_special_characters, remove_stopwords

class TestDataProcessing(unittest.TestCase):
    def test_preprocess_data(self):
        input_text = "This is a sample text."
        expected_output = "sample text"
        self.assertEqual(preprocess_data(input_text), expected_output)
        
    def test_remove_special_characters(self):
        input_text = "This is a $%& sample text!"
        expected_output = "This is a sample text"
        self.assertEqual(remove_special_characters(input_text), expected_output)
        
    def test_remove_stopwords(self):
        input_tokens = ["this", "is", "a", "sample", "text"]
        expected_output = ["sample", "text"]
        self.assertEqual(remove_stopwords(input_tokens), expected_output)

if __name__ == "__main__":
    unittest.main()
