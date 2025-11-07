# 🧠 AI Sentiment Analyzer

An intelligent **AI Sentiment Analyzer** built using **Python**, **Machine Learning**, and a beautiful **Streamlit web interface** that detects whether text input is **Positive**, **Negative**, or **Neutral**.

This project demonstrates how Natural Language Processing (NLP) can help interpret emotions in written text — a practical step into real-world AI applications such as feedback analysis, chatbots, and social media monitoring.

---

## 🌍 Project Overview

The **AI Sentiment Analyzer** takes a user’s input text and predicts its sentiment category using an NLP-based model.  
It also visualizes sentiment probabilities through interactive charts and features a **modern, startup-style interface** with smooth animations and gradient backgrounds.

The app runs entirely in the browser using **Streamlit**, so there’s no need for backend hosting — perfect for portfolios and AI demos.

---

## 💡 Concept

Sentiment Analysis is the process of determining whether a piece of text expresses a **positive**, **negative**, or **neutral** emotion.  
This app uses a trained **Machine Learning model** combined with **TextBlob**’s NLP capabilities to classify text sentiment.

Example use cases:
- Understanding customer feedback.
- Analyzing social media comments.
- Assessing product reviews or chat responses.
- Demonstrating NLP concepts in a visually appealing interface.

---

## 🧰 Tech Stack

| Category | Tools & Technologies |
|-----------|----------------------|
| **Programming Language** | Python 3.12 |
| **Frontend Framework** | Streamlit |
| **Machine Learning / NLP** | TextBlob, scikit-learn |
| **Visualization** | Matplotlib |
| **Data Handling** | Pandas |
| **Model Serialization** | Joblib |
| **Styling & UI** | Streamlit Theming, CSS (gradient overlay + dark mode) |
| **Version Control** | Git & GitHub |

---

## 📦 Python Packages Used

All these are listed in `requirements.txt`:
streamlit==1.31.0
textblob
matplotlib
pandas
scikit-learn
joblib


Each plays a key role:

| Package | Purpose |
|----------|----------|
| **Streamlit** | For building and running the web app interface |
| **TextBlob** | For natural language processing and sentiment scoring |
| **scikit-learn** | For model training and vectorization |
| **Pandas** | For loading and handling datasets |
| **Matplotlib** | For visualizing sentiment predictions in pie charts |
| **Joblib** | For saving and loading trained ML models efficiently |

---

## 🧩 Folder Structure

sentiment-analyzer/
│
├── data/
│ ├── train.csv
│ ├── test.csv
│
├── models/
│ ├── sentiment_model.pkl
│ ├── vectorizer.pkl
│
├── src/
│ ├── init.py
│ ├── app.py # Streamlit UI
│ ├── prepare_data.py # Data preprocessing and cleaning
│ ├── train.py # Model training script
│ ├── predict.py # Prediction logic
│ ├── config.py # File paths and configuration
│
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/ (excluded from Git)


---

## 🧠 How It Works (Step-by-Step)

1. **Data Preparation:**  
   The app uses simple labeled sentences from the training dataset to learn positive, negative, and neutral word associations.

2. **Feature Extraction:**  
   Text is transformed into numeric form using `TfidfVectorizer`.

3. **Model Training:**  
   A logistic regression classifier (from scikit-learn) is trained to detect sentiment polarity.

4. **Prediction:**  
   When a user enters a sentence, the model predicts the probability of each sentiment class.

5. **Visualization:**  
   A pie chart is generated showing the sentiment probability distribution.

6. **Interface & Theming:**  
   The Streamlit app includes an elegant gradient header, emoji-based feedback, and a dark/light theme toggle for better UX.

---

🧠 Example Inputs & Outputs
Input Sentence	Predicted Sentiment
"I love this app!"	😊 Positive
"This is terrible."	😠 Negative
"It’s okay, not bad."	😐 Neutral
"I feel amazing today!"	😊 Positive
"I don’t know how I feel."	😐 Neutral


🎨 Interface Highlights

🧠 Gradient Header with Icon
🌗 Dark / Light Theme Toggle (icon-based)
📊 Dynamic Pie Chart showing sentiment distribution
💬 Interactive real-time prediction
💻 Fully browser-based (no backend setup needed)
