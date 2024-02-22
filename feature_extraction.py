# utils/feature_extraction.py

from sklearn.feature_extraction.text import TfidfVectorizer

def extract_features(texts):
    # Extract TF-IDF features from text data
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(texts)
    return features
