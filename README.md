# 🛒 Fake Product Review Detection using Machine Learning

> A Full-Stack Web Application that identifies whether a product review is **Genuine** or **Fake** using **Machine Learning**, **Natural Language Processing (NLP)**, **Spring Boot**, and **Flask**.

---

## 📖 Overview

Online shopping platforms receive millions of product reviews every day. Unfortunately, many of these reviews are fake or misleading, influencing customer purchasing decisions.

This project leverages **Machine Learning** and **Natural Language Processing (NLP)** to automatically classify product reviews as **Genuine** or **Fake**. The application combines a responsive frontend, a Spring Boot backend, and a Flask-based ML API to provide real-time predictions.

---

## ✨ Key Features

- 🔐 User Login
- 📝 Product Review Analysis
- 🤖 Machine Learning-Based Prediction
- 📊 Confidence Score Display
- ⚡ Real-Time Review Classification
- 🔄 REST API Integration
- 📱 Responsive User Interface
- 🧹 NLP-Based Text Preprocessing

---

# 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Backend** | Java, Spring Boot, Maven |
| **Machine Learning** | Python, Flask, Scikit-learn |
| **NLP** | NLTK, TF-IDF |
| **Libraries** | Pandas, NumPy, Joblib |
| **Database** | MongoDB *(Optional)* |
| **Tools** | Git, GitHub, VS Code, Postman |

---

# 🏗️ System Architecture

```text
                   ┌─────────────┐
                   │    User     │
                   └──────┬──────┘
                          │
                          ▼
          ┌───────────────────────────┐
          │ HTML • CSS • JavaScript   │
          │       Frontend UI         │
          └───────────┬───────────────┘
                      │
                      ▼
          ┌───────────────────────────┐
          │     Spring Boot API       │
          └───────────┬───────────────┘
                      │ REST API
                      ▼
          ┌───────────────────────────┐
          │       Flask ML API        │
          └───────────┬───────────────┘
                      │
                      ▼
          ┌───────────────────────────┐
          │ TF-IDF + Logistic Regression │
          └───────────┬───────────────┘
                      │
                      ▼
          Genuine Review / Fake Review
```

---

# 🔄 Application Workflow

```text
User Login
      │
      ▼
Enter Product Review
      │
      ▼
Frontend Sends Review
      │
      ▼
Spring Boot Backend
      │
      ▼
Flask Machine Learning API
      │
      ▼
NLP Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Logistic Regression Prediction
      │
      ▼
Prediction + Confidence Score
      │
      ▼
Displayed to User
```

---

# 🧠 Machine Learning Pipeline

```
Dataset Collection
        │
        ▼
Data Cleaning
        │
        ▼
Text Preprocessing
        │
        ▼
TF-IDF Feature Extraction
        │
        ▼
Model Training
(Logistic Regression)
        │
        ▼
Model Serialization (Joblib)
        │
        ▼
Prediction using Flask API
```

---

# 📖 NLP Techniques Used

- ✅ Lowercase Conversion
- ✅ Text Cleaning
- ✅ Removing Special Characters
- ✅ Stop Word Removal
- ✅ TF-IDF Vectorization
- ✅ Text Classification

---

# 📂 Project Structure

```text
Fake-Product-Review-Detection/
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── style.css
│   ├── script.js
│   └── login.js
│
├── springboot-backend/
│
├── flask-api/
│   ├── app.py
│   ├── fake_review_model.pkl
│   ├── tfidf_vectorizer.pkl
│   ├── requirements.txt
│   └── model/
│
└── README.md
```

---

# 🚀 Getting Started

## 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/Fake-Product-Review-Detection.git

cd Fake-Product-Review-Detection
```

---

## 2️⃣ Start Flask API

```bash
pip install -r requirements.txt

python app.py
```

---

## 3️⃣ Start Spring Boot Backend

```bash
mvn spring-boot:run
```

---

## 4️⃣ Run Frontend

Simply open

```
index.html
```

using **Live Server** or any local web server.

---

# 📊 Sample Prediction

### Input Review

```text
This phone has an excellent battery life and great performance.
```

### Prediction

```text
Prediction : Genuine

Confidence : 96.45%
```

---

# 🎯 Advantages

- Detects fake product reviews automatically.
- Helps customers make informed purchasing decisions.
- Improves trust in e-commerce platforms.
- Lightweight and fast prediction model.
- Easy to integrate with other applications.

---

# 🔮 Future Enhancements

- 👤 User Registration
- 🔑 JWT Authentication
- 📜 Review History
- 📊 Admin Dashboard
- ☁️ Cloud Deployment
- 🤖 Deep Learning Models
- 🧠 BERT-based NLP Models
- 📈 Model Performance Analytics

---

# 👨‍💻 Authors

**Developed by**

- Rampathoti AjithKumar

---

# 📜 License

This project is developed for **educational and learning purposes**.

---

## ⭐ If you like this project, don't forget to Star the repository!
