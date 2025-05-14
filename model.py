import re, string
import joblib

# Load the trained model
model = joblib.load("news_classifier.pkl")

# Preprocess function (same one used during training)
def preprocess_text(text):
    text = text.lower()
    text = re.sub(rf"[{string.punctuation}]", "", text)
    text = re.sub(r"\d+", "", text)
    return text

# Predict function
def predict_category(text):
    clean_text = preprocess_text(text)
    pred = model.predict([clean_text])[0]
    confidence = model.predict_proba([clean_text]).max()
    return pred, round(float(confidence), 2)
