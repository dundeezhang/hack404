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
        article_title = article.get("title", "")
        article_author = article.get("author", "")
        article_date = article.get("publishedAt")
        article_description = article.get("description", "")
        article_publisher = article.get("source", {}).get("name", "")
        article_tags = generate_article_tags(article.get("content", ""))

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
            "health": False, "business": False, "entertainment": False}
    for word in words:
        word_lower = word.lower()
        tag_keywords = {
            "science": ["science"],
            "technology": ["tech", "technology", "technologies", "technological"],
            "health": ["health"],
            "business": ["business"],
            "entertainment": ["entertainment"],
            'discovery': ["discovery", "discoveries"],
            'innovation': ["innovation", "innovations"],
            'research': ["research", "studies", "study"],
            'breakthrough': ["breakthrough", "breakthroughs"],
            'advancement': ["advancement", "advancements"],
            'development': ["development", "developments"],
            'improvement': ["improvement", "improvements"],
            'finding': ["finding", "findings"],
        }

        for tag, keywords in tag_keywords.items():
            if any(keyword in word_lower for keyword in keywords):
                tags[tag] = True

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
