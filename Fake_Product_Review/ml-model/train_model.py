import pandas as pd
import re
import nltk
import joblib

from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Download stopwords (only first time)
nltk.download('stopwords')

# Load Dataset
df = pd.read_excel("../Datasets/Fake_Product_Review_Dataset_5000.xlsx")

# Load stopwords
stop_words = set(stopwords.words("english"))

# Function to clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# Apply cleaning
df["clean_review"] = df["review_text"].apply(clean_text)

# Features and Labels
X = df["clean_review"]
y = df["label"]

# Convert text into numbers using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Machine Learning Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make Predictions
y_pred = model.predict(X_test)

# Evaluate Model
print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(model, "fake_review_model.pkl")

# Save the TF-IDF vectorizer
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("\nModel saved successfully!")