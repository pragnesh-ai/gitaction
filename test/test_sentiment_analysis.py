from sentiment_analysis import analyze_sentiment

def test_analyze_sentiment_positive():
    polarity, classification = analyze_sentiment("I love this product! It's amazing.")
    assert polarity > 0
    assert classification == "positive"

def test_analyze_sentiment_negative():
    polarity, classification = analyze_sentiment("This movie was terrible. I hated it.")
    assert polarity < 0
    assert classification == "negative"

def test_analyze_sentiment_neutral():
    polarity, classification = analyze_sentiment("This is a neutral comment.")
    assert polarity == 0
    assert classification == "neutral"
