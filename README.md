# Reddit Sentiment Analysis Microservice

This microservice provides a RESTful API for analyzing sentiment in comments from a Reddit-like platform. It identifies if comments on a given subfeddit or category are positive, negative, or neutral.

## Installation

1. Clone the repository:

    '''bash
    git clone https://github.com/your-username/reddit-sentiment-analysis.git
    '''

2. Install dependencies using pip:

    '''bash
    pip install -r requirements.txt
    '''

3. Start the Flask application:

    '''bash
    python app.py
    '''

## API Endpoints

### Get Recent Comments

#### Request

- Method: 'GET'
- URL: '/api/v1/recent_comments/<subfeddit_id>'
- Parameters:
    - 'limit' (optional): Number of comments to retrieve (default: 25)
    - 'skip' (optional): Number of comments to skip (default: 0)
    - 'start_time' (optional): Start time for filtering comments by time range (Unix timestamp)
    - 'end_time' (optional): End time for filtering comments by time range (Unix timestamp)

#### Response

- Status Code: '200 OK' on success, '500 Internal Server Error' on failure
- Body: JSON array containing the most recent comments with sentiment analysis:

    '''json
    [
        {
            "id": 123,
            "text": "This is a positive comment!",
            "polarity_score": 0.8,
            "classification": "positive"
        },
        {
            "id": 124,
            "text": "This is a negative comment!",
            "polarity_score": -0.5,
            "classification": "negative"
        },
        ...
    ]
    '''

## Error Handling

- If there's an error fetching comments or analyzing sentiment, the API returns a JSON response with an error message and a status code of '500'.

## Logging

- The application logs errors and exceptions to the console using the Python 'logging' module.

## Contributing

1. Fork the repository
2. Create a new branch ('git checkout -b feature/new-feature')
3. Make changes and commit ('git commit -am 'Add new feature'')
4. Push to the branch ('git push origin feature/new-feature')
5. Create a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
