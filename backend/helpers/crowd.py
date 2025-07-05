import os
from dotenv import load_dotenv
from supabase import create_client, Client
import threading
from concurrent.futures import ThreadPoolExecutor

load_dotenv()

# init supabase
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
        
        # create new article record
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
        
        # ensure articles are all saved
        for future in futures:
            try:
                future.result(timeout=1) 
            except Exception:
                pass 
    
    background_thread = threading.Thread(target=save_batch)
    background_thread.daemon = True
    background_thread.start()