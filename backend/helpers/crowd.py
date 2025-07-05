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
        
        existing = supabase.table("articles").select("id").eq("link", article_url).execute()
        
        if existing.data:
            return existing.data[0]["id"]
        
        article_data = {
            "link": article_url,
            "likes": 0,
            "dislikes": 0
        }
        
        result = supabase.table("articles").insert(article_data).execute()
        return result.data[0]["id"] if result.data else None
        
    except Exception as e:
        error_msg = str(e)
        if "row-level security policy" in error_msg.lower():
            print(f"RLS Policy Error: Make sure your Supabase service role key is configured, or disable RLS on the articles table")
        else:
            print(f"Error saving article to database: {error_msg}")
        return None

def save_articles_batch(articles):
    def save_batch():
        futures = []
        for article in articles:
            future = db_executor.submit(save_article_to_db_sync, article)
            futures.append(future)
        
        for future in futures:
            try:
                future.result(timeout=1) 
            except Exception:
                pass 
    
    background_thread = threading.Thread(target=save_batch)
    background_thread.daemon = True
    background_thread.start()

def get_article_id_by_url(article_url):
    try:
        if not article_url:
            return None
        
        result = supabase.table("articles").select("id").eq("link", article_url).execute()
        
        if result.data:
            return result.data[0]["id"]
        
        article_data = {
            "link": article_url,
            "likes": 0,
            "dislikes": 0
        }
        
        insert_result = supabase.table("articles").insert(article_data).execute()
        return insert_result.data[0]["id"] if insert_result.data else None
        
    except Exception as e:
        error_msg = str(e)
        if "row-level security policy" in error_msg.lower():
            print(f"RLS Policy Error: Make sure your Supabase service role key is configured, or disable RLS on the articles table")
        else:
            print(f"Error searching for article: {error_msg}")
        return None

def update_article_likes(article_url, increment: bool):
    try:
        if not article_url:
            return None
        
        # Get article ID from URL
        article_id = get_article_id_by_url(article_url)
        if not article_id:
            print(f"Could not find or create article for URL: {article_url}")
            return None
        
        current_result = supabase.table("articles").select("likes").eq("id", article_id).execute()
        
        if not current_result.data:
            print(f"Article with ID {article_id} not found")
            return None
        
        current_likes = current_result.data[0]["likes"]
        new_likes = current_likes + 1 if increment else max(0, current_likes - 1)
        update_result = supabase.table("articles").update({"likes": new_likes}).eq("id", article_id).execute()
        
        if update_result.data:
            return new_likes
        else:
            print(f"Failed to update likes for article {article_id}")
            return None
            
    except Exception as e:
        error_msg = str(e)
        if "row-level security policy" in error_msg.lower():
            print(f"RLS Policy Error: Make sure your Supabase service role key is configured, or disable RLS on the articles table")
        else:
            print(f"Error updating article likes: {error_msg}")
        return None

def update_article_dislikes(article_url, increment: bool):
    try:
        if not article_url:
            return None
        
        # Get article ID from URL
        article_id = get_article_id_by_url(article_url)
        if not article_id:
            print(f"Could not find or create article for URL: {article_url}")
            return None
        
        current_result = supabase.table("articles").select("dislikes").eq("id", article_id).execute()
        
        if not current_result.data:
            print(f"Article with ID {article_id} not found")
            return None
        
        current_dislikes = current_result.data[0]["dislikes"]
        new_dislikes = current_dislikes + 1 if increment else max(0, current_dislikes - 1)
        update_result = supabase.table("articles").update({"dislikes": new_dislikes}).eq("id", article_id).execute()
        
        if update_result.data:
            return new_dislikes
        else:
            print(f"Failed to update dislikes for article {article_id}")
            return None
            
    except Exception as e:
        error_msg = str(e)
        if "row-level security policy" in error_msg.lower():
            print(f"RLS Policy Error: Make sure your Supabase service role key is configured, or disable RLS on the articles table")
        else:
            print(f"Error updating article dislikes: {error_msg}")
        return None