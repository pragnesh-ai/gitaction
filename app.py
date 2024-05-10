from flask import Flask, jsonify, request
import requests
from textblob import TextBlob

app = Flask(__name__)

def get_recent_comments(subfeddit_id, limit=25, skip=0, start_time=None, end_time=None):
    url = f'http://localhost:8080/api/v1/comments/?subfeddit_id={subfeddit_id}&limit={limit}&skip={skip}'
    if start_time:
        url += f'&start_time={start_time}'
    if end_time:
        url += f'&end_time={end_time}'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        comments = data.get('comments', [])
        
        # Sort comments by created_at timestamp in descending order
        sorted_comments = sorted(comments, key=lambda x: x['created_at'], reverse=True)
        
        return sorted_comments
    else:
        return []

def analyze_sentiment(comment_text):
    """
    Analyzes the sentiment of a given comment text.

    Parameters:
        comment_text (str): The text of the comment to analyze.

    Returns:
        tuple: A tuple containing the polarity score and classification.
            The polarity score is a float between -1.0 and 1.0.
            The classification is a string indicating 'positive', 'negative', or 'neutral'.
    """
    blob = TextBlob(comment_text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        classification = "positive"
    elif polarity < 0:
        classification = "negative"
    else:
        classification = "neutral"

    return polarity, classification

@app.route('/api/v1/recent_comments/<int:subfeddit_id>', methods=['GET'])
def recent_comments(subfeddit_id):
    limit = int(request.args.get('limit', 25))
    skip = int(request.args.get('skip', 0))
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    
    comments = get_recent_comments(subfeddit_id, limit, skip, start_time, end_time)
    
    # Perform sentiment analysis and classify comments
    classified_comments = []
    for comment in comments:
        polarity_score, classification = analyze_sentiment(comment["text"])
        classified_comments.append({
            "id": comment["id"],
            "text": comment["text"],
            "polarity_score": polarity_score,
            "classification": classification
        })
    
    return jsonify(classified_comments)

if __name__ == '__main__':
    app.run(debug=True)
