from selenium import webdriver
from selenium.webdriver.common.by import By

def crawl_page(url):
    """
    Crawl a webpage and return its content as a string.
    
    Args:
        url (str): The URL to crawl
        
    Returns:
        str: String containing the page body content
    """
    driver = webdriver.Chrome()
    
    try:
        driver.get(url)
        
        # Get the body element content
        body_element = driver.find_element(By.TAG_NAME, "body")
        body_content = body_element.text
        
        return body_content
        
    finally:
        driver.quit()
