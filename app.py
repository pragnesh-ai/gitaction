from flask import Flask, jsonify, request
import requests
from textblob import TextBlob
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

def get_recent_comments(subfeddit_id, limit=25, skip=0, start_time=None, end_time=None):
    try:
        url = f'http://localhost:8080/api/v1/comments/?subfeddit_id={subfeddit_id}&limit={limit}&skip={skip}'
        if start_time:
            url += f'&start_time={start_time}'
        if end_time:
            url += f'&end_time={end_time}'
        
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for non-200 status codes
        
        data = response.json()
        comments = data.get('comments', [])
        
        # Sort comments by created_at timestamp in descending order
        sorted_comments = sorted(comments, key=lambda x: x['created_at'], reverse=True)
        
        # Perform sentiment analysis and classify comments
        classified_comments = []
        for comment in sorted_comments:
            polarity_score, classification = analyze_sentiment(comment["text"])
            comment.update({
                "polarity_score": polarity_score,
                "classification": classification
            })
            classified_comments.append(comment)
        
        return classified_comments
    except Exception as e:
        logging.error(f"Failed to fetch recent comments: {e}")
        return []

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

@app.route('/api/v1/recent_comments/<int:subfeddit_id>', methods=['GET'])
def recent_comments(subfeddit_id):
    try:
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
    except Exception as e:
        logging.error(f"Failed to process recent comments request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=False)
