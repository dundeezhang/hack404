from fastapi import FastAPI, HTTPException
import requests
import os
from dotenv import load_dotenv

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

@app.get("/get")
def get_news(ignore: str = "", search: str = ""):
    api_key = os.getenv("NEWSAPI_KEY")
    
    if not api_key:
        raise HTTPException(status_code=500, detail="NewsAPI key not configured")
    
    ignore_list = [keyword.strip() for keyword in ignore.split(",") if keyword.strip()]
    search_list = [keyword.strip() for keyword in search.split(",") if keyword.strip()]
    
    url = "https://newsapi.org/v2/top-headlines"
    
    params = {
        "apiKey": api_key,
        "pageSize": 100,
        "country" : "us",
        "category": "general",
        "language": "en" 
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        news_data = response.json()
        
        filtered_articles = filter_articles(news_data.get("articles", []), ignore_list, search_list)
        
        return {
            "status": "success",
            "totalResults": len(filtered_articles),
            "originalTotalResults": news_data.get("totalResults", 0),
            "articles": filtered_articles
        }
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching news: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@app.get("/get_business")
def get_business(ignore: str = "", search: str = ""):
    api_key = os.getenv("NEWSAPI_KEY")
    
    if not api_key:
        raise HTTPException(status_code=500, detail="NewsAPI key not configured")
    
    ignore_list = [keyword.strip() for keyword in ignore.split(",") if keyword.strip()]
    search_list = [keyword.strip() for keyword in search.split(",") if keyword.strip()]
    
    url = "https://newsapi.org/v2/top-headlines"
    
    params = {
        "apiKey": api_key,
        "pageSize": 100,
        "country": "us",
        "category": "business",
        "language": "en" 
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        news_data = response.json()
        
        filtered_articles = filter_articles(news_data.get("articles", []), ignore_list, search_list)
        
        return {
            "status": "success",
            "totalResults": len(filtered_articles),
            "originalTotalResults": news_data.get("totalResults", 0),
            "articles": filtered_articles
        }
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching business news: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@app.get("/get_entertainment")
def get_entertainment(ignore: str = "", search: str = ""):
    api_key = os.getenv("NEWSAPI_KEY")
    
    if not api_key:
        raise HTTPException(status_code=500, detail="NewsAPI key not configured")
    
    ignore_list = [keyword.strip() for keyword in ignore.split(",") if keyword.strip()]
    search_list = [keyword.strip() for keyword in search.split(",") if keyword.strip()]
    
    url = "https://newsapi.org/v2/top-headlines"
    
    params = {
        "apiKey": api_key,
        "pageSize": 100,
        "country": "us",
        "category": "entertainment",
        "language": "en" 
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        news_data = response.json()
        
        filtered_articles = filter_articles(news_data.get("articles", []), ignore_list, search_list)
        
        return {
            "status": "success",
            "totalResults": len(filtered_articles),
            "originalTotalResults": news_data.get("totalResults", 0),
            "articles": filtered_articles
        }
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching entertainment news: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@app.get("/get_general")
def get_general(ignore: str = "", search: str = ""):
    api_key = os.getenv("NEWSAPI_KEY")
    
    if not api_key:
        raise HTTPException(status_code=500, detail="NewsAPI key not configured")
    
    ignore_list = [keyword.strip() for keyword in ignore.split(",") if keyword.strip()]
    search_list = [keyword.strip() for keyword in search.split(",") if keyword.strip()]
    
    url = "https://newsapi.org/v2/top-headlines"
    
    params = {
        "apiKey": api_key,
        "pageSize": 100,
        "country": "us",
        "category": "general",
        "language": "en" 
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        news_data = response.json()
        
        filtered_articles = filter_articles(news_data.get("articles", []), ignore_list, search_list)
        
        return {
            "status": "success",
            "totalResults": len(filtered_articles),
            "originalTotalResults": news_data.get("totalResults", 0),
            "articles": filtered_articles
        }
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching general news: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@app.get("/get_health")
def get_health(ignore: str = "", search: str = ""):
    api_key = os.getenv("NEWSAPI_KEY")
    
    if not api_key:
        raise HTTPException(status_code=500, detail="NewsAPI key not configured")
    
    ignore_list = [keyword.strip() for keyword in ignore.split(",") if keyword.strip()]
    search_list = [keyword.strip() for keyword in search.split(",") if keyword.strip()]
    
    url = "https://newsapi.org/v2/top-headlines"
    
    params = {
        "apiKey": api_key,
        "pageSize": 100,
        "country": "us",
        "category": "health",
        "language": "en" 
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        news_data = response.json()
        
        filtered_articles = filter_articles(news_data.get("articles", []), ignore_list, search_list)
        
        return {
            "status": "success",
            "totalResults": len(filtered_articles),
            "originalTotalResults": news_data.get("totalResults", 0),
            "articles": filtered_articles
        }
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching health news: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@app.get("/get_science")
def get_science(ignore: str = "", search: str = ""):
    api_key = os.getenv("NEWSAPI_KEY")
    
    if not api_key:
        raise HTTPException(status_code=500, detail="NewsAPI key not configured")
    
    ignore_list = [keyword.strip() for keyword in ignore.split(",") if keyword.strip()]
    search_list = [keyword.strip() for keyword in search.split(",") if keyword.strip()]
    
    url = "https://newsapi.org/v2/top-headlines"
    
    params = {
        "apiKey": api_key,
        "pageSize": 100,
        "country": "us",
        "category": "science",
        "language": "en" 
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        news_data = response.json()
        
        filtered_articles = filter_articles(news_data.get("articles", []), ignore_list, search_list)
        
        return {
            "status": "success",
            "totalResults": len(filtered_articles),
            "originalTotalResults": news_data.get("totalResults", 0),
            "articles": filtered_articles
        }
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching science news: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@app.get("/get_sports")
def get_sports(ignore: str = "", search: str = ""):
    api_key = os.getenv("NEWSAPI_KEY")
    
    if not api_key:
        raise HTTPException(status_code=500, detail="NewsAPI key not configured")
    
    ignore_list = [keyword.strip() for keyword in ignore.split(",") if keyword.strip()]
    search_list = [keyword.strip() for keyword in search.split(",") if keyword.strip()]
    
    url = "https://newsapi.org/v2/top-headlines"
    
    params = {
        "apiKey": api_key,
        "pageSize": 100,
        "country": "us",
        "category": "sports",
        "language": "en" 
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        news_data = response.json()
        
        filtered_articles = filter_articles(news_data.get("articles", []), ignore_list, search_list)
        
        return {
            "status": "success",
            "totalResults": len(filtered_articles),
            "originalTotalResults": news_data.get("totalResults", 0),
            "articles": filtered_articles
        }
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching sports news: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@app.get("/get_technology")
def get_technology(ignore: str = "", search: str = ""):
    api_key = os.getenv("NEWSAPI_KEY")
    
    if not api_key:
        raise HTTPException(status_code=500, detail="NewsAPI key not configured")
    
    ignore_list = [keyword.strip() for keyword in ignore.split(",") if keyword.strip()]
    search_list = [keyword.strip() for keyword in search.split(",") if keyword.strip()]
    
    url = "https://newsapi.org/v2/top-headlines"
    
    params = {
        "apiKey": api_key,
        "pageSize": 100,
        "country": "us",
        "category": "technology",
        "language": "en" 
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        news_data = response.json()
        
        filtered_articles = filter_articles(news_data.get("articles", []), ignore_list, search_list)
        
        return {
            "status": "success",
            "totalResults": len(filtered_articles),
            "originalTotalResults": news_data.get("totalResults", 0),
            "articles": filtered_articles
        }
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching technology news: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")