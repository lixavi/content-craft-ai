# tests/test_model_evaluation.py

import unittest
from utils.model_evaluation import evaluate_model

class TestModelEvaluation(unittest.TestCase):
    def test_evaluate_model(self):
        # Test evaluating model with perfect predictions
        predictions = ["positive", "negative", "positive", "negative"]
        labels = ["positive", "negative", "positive", "negative"]
        accuracy = evaluate_model(predictions, labels)
        self.assertEqual(accuracy, 1.0)

    def test_evaluate_model_mismatched_lengths(self):
        # Test evaluating model with mismatched lengths of predictions and labels
        predictions = ["positive", "negative", "positive"]
        labels = ["positive", "negative", "positive", "negative"]
        with self.assertRaises(ValueError):
            evaluate_model(predictions, labels)

    def test_evaluate_model_partial_match(self):
        # Test evaluating model with partial match of predictions and labels
        predictions = ["positive", "negative", "positive", "negative"]
        labels = ["positive", "negative", "positive", "positive"]
        accuracy = evaluate_model(predictions, labels)
        self.assertEqual(accuracy, 0.75)

if __name__ == "__main__":
    unittest.main()
