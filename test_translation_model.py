# tests/test_translation_model.py

import unittest
from models.translation_model import TranslationModel

class TestTranslationModel(unittest.TestCase):
    def test_translate_text(self):
        # Test translating text from English to French
        translation_model = TranslationModel()
        input_text = "Hello, how are you?"
        translated_text = translation_model.translate_text(input_text, source_lang="en", target_lang="fr")
        self.assertTrue(isinstance(translated_text, str))
        self.assertNotEqual(input_text, translated_text)

    def test_translate_text_with_custom_model(self):
        # Test translating text using a custom model
        custom_model_name = "t5-base"
        translation_model = TranslationModel(model_name=custom_model_name)
        input_text = "Hello, how are you?"
        translated_text = translation_model.translate_text(input_text, source_lang="en", target_lang="fr")
        self.assertTrue(isinstance(translated_text, str))
        self.assertNotEqual(input_text, translated_text)

if __name__ == "__main__":
    unittest.main()
