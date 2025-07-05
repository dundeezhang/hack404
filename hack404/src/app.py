import json
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/news", methods=['GET'])
def get_articles():
    category = request.args.get('category', 'general')
    ignore  = request.args.get('ignore', '')
    search = request.args.get('search', '')

    fastapi_url = "http://localhost:8000/news"
    params = { 
        'category': category,
        'ignore': ignore,
        'search': search
    }

    try:
        response = requests.get(fastapi_url, params=params)
        response.raise_for_status()
        news_data = response.json()

        articles = []
        for article in news_data.get('articles', []):
            articles.append({
                "imageUrl": article.get('urlToImage', ''),
                "title": article.get('title', ''),
                "author": {
                    "first": article.get('author', '').split()[0] if article.get('author') else '',
                    "last": ' '.join(article.get('author', '').split()[1:]) if article.get('author') else '',
                },
                "date": article.get('publishedAt', ''),
                "filters": [category],
            })
        return jsonify(articles)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch news: {str(e)}"}), 500
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)

