from flask import Flask, request, jsonify
import joblib
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords (only first time)
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Create Flask app
app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("fake_review_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Text cleaning function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    review = data["review"]

    clean_review = clean_text(review)

    review_vector = vectorizer.transform([clean_review])

    prediction = model.predict(review_vector)[0]

    confidence = max(model.predict_proba(review_vector)[0]) * 100

    return jsonify({
        "prediction": prediction,
        "confidence": round(confidence, 2)
    })

# Run Flask server
if __name__ == "__main__":
    app.run(debug=True)