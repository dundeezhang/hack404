from fastapi import FastAPI, HTTPException
import requests
import os
from dotenv import load_dotenv
from helpers.scan import scan_website
from helpers.database import save_articles_batch, get_article_id_by_url, update_article_dislikes, update_article_likes, get_dislike_count, get_like_count, get_top_articles, get_article_tag
from helpers.filter import filter_articles
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Local development server
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def use_the_api_better():
    return {"get better": "dundee"}


@app.get("/news")
def get_news_by_category(category: str = "general", ignore: str = "", search: str = ""):
    """
    Get news from NewsAPI by category with filtering by categories and options
    Args:
        category: general, business, entertainment, general, health, science, sports, technology
        ignore: Comma-separated keywords to filter OUT
        search: Comma-separated keywords to filter IN
    Returns:
        JSON response with filtered news articles
    """
    api_key = os.getenv("NEWSAPI_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500, detail="NewsAPI key not configured")

    # Validate category
    valid_categories = ["business", "entertainment",
                        "general", "health", "science", "sports", "technology"]
    if category not in valid_categories:
        raise HTTPException(
            status_code=400, detail=f"Invalid category. Must be one of: {', '.join(valid_categories)}")

    ignore_list = [keyword.strip()
                   for keyword in ignore.split(",") if keyword.strip()]
    search_list = [keyword.strip()
                   for keyword in search.split(",") if keyword.strip()]

    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "apiKey": api_key,
        "pageSize": 100,
        "country": "us",
        "category": category,
        "language": "en",
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        news_data = response.json()

        filtered_articles = filter_articles(
            news_data.get("articles", []), ignore_list, search_list, category)
        save_articles_batch(filtered_articles)

        return {
            "status": "success",
            "category": category,
            "totalResults": len(filtered_articles),
            "originalTotalResults": news_data.get("totalResults", 0),
            "articles": filtered_articles
        }

    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching {category} news: {str(e)}")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {str(e)}")


@app.get("/get-article-id")
def get_article_id(url: str = ''):
    """
    Search for an article by URL and return its UUID/ID.
    Args:
        article_url (str): The URL of the article to search for 
    Returns:
        str: The UUID/ID of the article if found
    """
    return get_article_id_by_url(url)


@app.get("/update-likes")
def update_likes(url: str = '', increment: bool = True):
    """
    Update likes for an article by URL.
    Args:
        url (str): The URL of the article to update likes for
        increment (bool): Whether to increment or decrement likes (default: True)
    Returns:
        int: The updated number of likes
    """
    return update_article_likes(url, increment)


@app.get("/update-dislikes")
def update_dislikes(url: str = '', increment: bool = True):
    """
    Update dislikes for an article by URL.
    Args:
        url (str): The URL of the article to update dislikes for
        increment (bool): Whether to increment or decrement dislikes (default: True)
    Returns:
        int: The updated number of dislikes
    """
    return update_article_dislikes(url, increment)


@app.get("/like-counts")
def like_counts(url: str):
    """
    Get the like count for an article by URL.
    Args:
        url (str): The URL of the article to get likes for
    Returns:
        int: The number of likes for the article
    """
    return get_like_count(url)


@app.get("/dislike-counts")
def dislike_counts(url: str):
    """
    Get the dislike count for an article by URL.
    Args:
        url (str): The URL of the article to get dislikes for
    Returns:
        int: The number of dislikes for the article
    """
    return get_dislike_count(url)


@app.get("/top-articles")
def top_articles_endpoint(limit: int):
    """
    Get the top articles based on likes.
    Args:
        limit (int): The number of top articles to return
    Returns:
        list: A list of top articles sorted by likes
    """
    return get_top_articles(limit)


@app.get("/scan-website")
def scan_website_endpoint(url: str):
    """
    Scan a website and return processed content.
    Args:
        url (str): The URL of the website to scan
    Returns:
        str: The processed content from the website
    """
    return scan_website(url)


@app.get("/article-tag")
def article_tag(url: str):
    """
    Get the tag for an article by URL.
    Args:
        url (str): The URL of the article to get the tag for
    Returns:
        str: The tag of the article if found, otherwise None
    """
    return get_article_tag(url)
