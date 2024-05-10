from textblob import TextBlob

# Dictionary to store text with polarity
text_polarity = {}

# Sample texts with unique identifiers
texts = {
    "text1": "I love this product! It's amazing.",
    "text2": "This movie was terrible. I hated it."
}

# Perform sentiment analysis for each text
for text_id, text in texts.items():
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    text_polarity[text_id] = polarity

# Print text with polarity
for text_id, polarity in text_polarity.items():
    print("Text ID:", text_id)
    print("Polarity:", polarity)
