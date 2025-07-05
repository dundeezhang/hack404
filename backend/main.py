from fastapi import FastAPI, HTTPException
import requests
import os
from dotenv import load_dotenv
from crawl import crawl_page

# Load environment variables
load_dotenv()

app = FastAPI()

def filter_articles(articles, ignore_list, search_list):
    """
    Filter articles by ignore and search criteria
    """
    filtered_articles = []
    ignore_keywords = [keyword.lower() for keyword in ignore_list]
    search_keywords = [keyword.lower() for keyword in search_list] if search_list else []
    
    for article in articles:
        title = (article.get("title") or "").lower()
        description = (article.get("description") or "").lower()
        content = (article.get("content") or "").lower()
        article_text = f"{title} {description} {content}"
        
        # Skip if contains any ignore keywords
        if ignore_keywords and any(keyword in article_text for keyword in ignore_keywords):
            continue
            
        # If search keywords specified, must contain at least one
        if search_keywords and not any(keyword in article_text for keyword in search_keywords):
            continue
            
        filtered_articles.append(article)
    
    return filtered_articles

@app.get("/")
def use_the_api_better():
    return {"get better": "dundee"}

@app.get("/news")
def get_news_by_category(category: str = "general", ignore: str = "", search: str = ""):
    """
    Get news from NewsAPI by category with filtering by categories and options
    
    Args:
        category: News category (default: "general")
                 Available categories: business, entertainment, general, health, science, sports, technology
        ignore: Comma-separated keywords to filter OUT from articles (default: "")
        search: Comma-separated keywords to filter IN - articles must contain at least one (default: "")
    
    Returns:
        JSON response with filtered news articles
    """
    api_key = os.getenv("NEWSAPI_KEY")
    
    if not api_key:
        raise HTTPException(status_code=500, detail="NewsAPI key not configured")
    
    # Validate category
    valid_categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    if category not in valid_categories:
        raise HTTPException(status_code=400, detail=f"Invalid category. Must be one of: {', '.join(valid_categories)}")
    
    ignore_list = [keyword.strip() for keyword in ignore.split(",") if keyword.strip()]
    search_list = [keyword.strip() for keyword in search.split(",") if keyword.strip()]
    
    url = "https://newsapi.org/v2/top-headlines"
    
    params = {
        "apiKey": api_key,
        "pageSize": 100,
        "country": "us",
        "category": category,
        "language": "en" 
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        news_data = response.json()
        
        filtered_articles = filter_articles(news_data.get("articles", []), ignore_list, search_list)
        
        return {
            "status": "success",
            "category": category,
            "totalResults": len(filtered_articles),
            "originalTotalResults": news_data.get("totalResults", 0),
            "articles": filtered_articles
        }
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching {category} news: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    
@app.get("/crawl")
def crawl(website: str = ""):
    """
    Crawl specific website
    Args:
        website: website to crawl
    Returns:
        string with website body
    """
    return crawl_page(website)

# Legacy endpoint for backward compatibility
@app.get("/get")
def get_news(ignore: str = "", search: str = ""):
    """Legacy endpoint - use /news instead"""
    return get_news_by_category("general", ignore, search)
