from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        return "Positive", {"Positive": 100, "Negative": 0, "Neutral": 0}
    elif polarity < -0.1:
        return "Negative", {"Positive": 0, "Negative": 100, "Neutral": 0}
    else:
        return "Neutral", {"Positive": 0, "Negative": 0, "Neutral": 100}
