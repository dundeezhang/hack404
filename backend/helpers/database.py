import os
import threading
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_service_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
if not supabase_service_key:
    supabase_service_key = os.getenv("SUPABASE_ANON_KEY")

supabase: Client = create_client(supabase_url, supabase_service_key)
db_executor = ThreadPoolExecutor(max_workers=5)


def save_article_to_db_sync(article):
    try:
        article_url = article.get("url") or article.get("link", "")

        if not article_url:
            return None

        existing = supabase.table("articles").select(
            "id").eq("link", article_url).execute()

        if existing.data:
            return existing.data[0]["id"]

        # Extract article data from the article object
        search_content = article.get(
            "content", "") + article.get("description", "") + article.get("category", "") + \
            article.get("title", "") + article.get("author", "") + \
            article.get("source", {}).get("name", "") + \
            article.get("publishedAt", "")
        article_title = article.get("title", "")
        article_author = article.get("author", "")
        article_date = article.get("publishedAt")
        article_description = article.get("description", "")
        article_publisher = article.get("source", {}).get("name", "")
        article_tags = generate_article_tags(search_content)

        article_data = {
            "link": article_url,
            "likes": 0,
            "dislikes": 0,
            "tags": article_tags,
            "title": article_title,
            "author": article_author or article_publisher,
            "description": article_description,
            "date_written": article_date
        }

        result = supabase.table("articles").insert(article_data).execute()
        return result.data[0]["id"] if result.data else None

    except:
        return None


def save_articles_batch(articles):
    def save_batch():
        futures = []
        for article in articles:
            future = db_executor.submit(save_article_to_db_sync, article)
            futures.append(future)

        for future in futures:
            try:
                future.result(timeout=2)
            except Exception:
                pass

    background_thread = threading.Thread(target=save_batch)
    background_thread.daemon = True
    background_thread.start()


def get_article_id_by_url(article_url):
    try:
        if not article_url:
            return None

        result = supabase.table("articles").select(
            "id").eq("link", article_url).execute()
        return result.data[0]["id"]

    except:
        return None


def update_article_likes(article_url, increment: bool):
    try:
        if not article_url:
            return None

        article_id = get_article_id_by_url(article_url)
        if not article_id:
            return None

        current_result = supabase.table("articles").select(
            "likes").eq("id", article_id).execute()

        if not current_result.data:
            return None

        current_likes = current_result.data[0]["likes"]
        new_likes = current_likes + \
            1 if increment else max(0, current_likes - 1)
        update_result = supabase.table("articles").update(
            {"likes": new_likes}).eq("id", article_id).execute()

        if update_result.data:
            return new_likes
        else:
            return None

    except:
        return None


def update_article_dislikes(article_url, increment: bool):
    try:
        if not article_url:
            return None

        article_id = get_article_id_by_url(article_url)
        if not article_id:
            return None

        current_result = supabase.table("articles").select(
            "dislikes").eq("id", article_id).execute()

        if not current_result.data:
            return None

        current_dislikes = current_result.data[0]["dislikes"]
        new_dislikes = current_dislikes + \
            1 if increment else max(0, current_dislikes - 1)
        update_result = supabase.table("articles").update(
            {"dislikes": new_dislikes}).eq("id", article_id).execute()

        if update_result.data:
            return new_dislikes
        else:
            return None

    except:
        return None


def get_like_count(article_url):
    try:
        if not article_url:
            return None

        article_id = get_article_id_by_url(article_url)
        if not article_id:
            return None

        result = supabase.table("articles").select(
            "likes").eq("id", article_id).execute()

        if result.data:
            return result.data[0]["likes"]
        else:
            return None

    except:
        return None


def get_dislike_count(article_url):
    try:
        if not article_url:
            return None

        article_id = get_article_id_by_url(article_url)
        if not article_id:
            return None

        result = supabase.table("articles").select(
            "dislikes").eq("id", article_id).execute()

        if result.data:
            return result.data[0]["dislikes"]
        else:
            return None

    except:
        return None


def generate_article_tags(body: str):
    words = body.split()

    # if len(words) > 200:
    #    words = words[:200]

    tags = {"science": False, "technology": False,
            "health": False, "business": False, "entertainment": False, "general": False}
    for word in words:
        word_lower = word.lower()
        tag_keywords = {
            "science": ["science", "discovery", "discoveries", "scientific", "scientists", "research", "study", "studies", "experiment", "laboratory", "physics", "chemistry", "biology", "astronomy", "climate", "environment", "space", "nasa", "breakthrough", "innovation", "genetics", "evolution", "quantum", "molecule", "atom", "ecosystem", "paleontology", "archaeology", "geology", "meteorology", "oceanography"],
            "technology": ["tech", "technology", "technologies", "technological", "gadget", "software", "hardware", "ai", "artificial intelligence", "machine learning", "blockchain", "cryptocurrency", "bitcoin", "startup", "silicon valley", "computer", "smartphone", "app", "application", "coding", "programming", "developer", "internet", "web", "digital", "cyber", "robot", "automation", "5g", "cloud", "data", "algorithm", "virtual reality", "augmented reality", "iot", "cybersecurity"],
            "health": ["health", "healthy", "healthcare", "wellness", "medical", "medicine", "disease", "diseases", "virus", "pandemic", "epidemic", "hospital", "doctor", "patient", "treatment", "therapy", "vaccine", "vaccination", "mental health", "fitness", "nutrition", "diet", "exercise", "surgery", "cancer", "diabetes", "heart", "brain", "pharmaceutical", "drug", "medication", "clinical", "diagnosis", "symptoms", "covid", "coronavirus", "flu", "infection"],
            "business": ["business", "economy", "economic", "economics", "financial", "finance", "market", "stock", "investment", "investor", "trading", "company", "corporation", "startup", "entrepreneur", "ceo", "revenue", "profit", "earnings", "growth", "merger", "acquisition", "ipo", "bankruptcy", "recession", "inflation", "gdp", "unemployment", "jobs", "employment", "industry", "manufacturing", "retail", "consumer", "sales", "marketing", "brand"],
            "entertainment": ["entertainment", "entertain", "entertaining", "entertains", "entertained", "showbiz", "show business", "movie", "film", "cinema", "tv", "television", "series", "netflix", "disney", "hollywood", "celebrity", "actor", "actress", "director", "music", "musician", "singer", "album", "concert", "festival", "gaming", "video games", "sports", "football", "basketball", "soccer", "olympics", "award", "oscar", "grammy", "streaming", "podcast"],
            "innovation": ["innovation", "innovations", "innovative", "breakthrough", "revolutionary", "cutting-edge", "pioneering", "groundbreaking", "advancement", "progress", "invention", "patent", "prototype", "disruptive", "emerging", "next-generation", "state-of-the-art", "novel", "creative", "solution"],
        }

        for tag, keywords in tag_keywords.items():
            if any(keyword in word_lower for keyword in keywords):
                tags[tag] = True

    if not any(tags.values()):
        tags["general"] = True

    return ",".join([f"{key}" for key, value in tags.items() if value])


def get_top_articles(limit: int):
    try:
        result = supabase.table("articles").select(
            "link, title, author, likes"
        ).order("likes", desc=True).limit(limit).execute()
        return result.data if result.data else []
    except:
        return []


def get_description(url: str):
    try:
        if not url:
            return None

        article_id = get_article_id_by_url(url)

        result = supabase.table("articles").select(
            "description").eq("id", article_id).execute()

        if result.data:
            return result.data[0]["description"]
        else:
            return None

    except:
        return None


def get_article_tag(url: str):
    try:
        if not url:
            return None

        article_id = get_article_id_by_url(url)

        result = supabase.table("articles").select(
            "tags").eq("id", article_id).execute()

        if result.data:
            return result.data[0]["tags"]
        else:
            return None

    except:
        return None
