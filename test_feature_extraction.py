# tests/test_feature_extraction.py

import unittest
from utils.feature_extraction import extract_features
from sklearn.feature_extraction.text import TfidfVectorizer

class TestFeatureExtraction(unittest.TestCase):
    def test_extract_features(self):
        # Test extracting features from text data
        texts = ["This is a test sentence.", "Another test sentence.", "Yet another test sentence."]
        expected_features = TfidfVectorizer().fit_transform(texts)
        extracted_features = extract_features(texts)
        self.assertEqual(extracted_features.shape, expected_features.shape)
        self.assertTrue((extracted_features != expected_features).nnz == 0)

if __name__ == "__main__":
    unittest.main()
