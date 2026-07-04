import re
import joblib
import nltk
from nltk.corpus import stopwords

# Download stopwords (only first time)
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Load saved model and vectorizer
model = joblib.load("fake_review_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# Take input from user
review = input("Enter Product Review: ")

# Clean review
clean_review = clean_text(review)

# Convert into TF-IDF
review_vector = vectorizer.transform([clean_review])

# Prediction
prediction = model.predict(review_vector)

# Probability
probability = model.predict_proba(review_vector)

print("\nPrediction :", prediction[0])
print("Confidence :", round(max(probability[0]) * 100, 2), "%")