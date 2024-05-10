from textblob import TextBlob
import logging

def analyze_sentiment(comment_text):
    try:
        blob = TextBlob(comment_text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            classification = "positive"
        elif polarity < 0:
            classification = "negative"
        else:
            classification = "neutral"

        return polarity, classification
    except Exception as e:
        logging.error(f"Failed to analyze sentiment: {e}")
        return 0, "neutral"
