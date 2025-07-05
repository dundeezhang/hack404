from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def crawl_page(url):
    try:
        driver.get(url)
        
        # get the body content
        body_element = driver.find_element(By.TAG_NAME, "body")
        body_content = body_element.text
        
        return body_content
        
    finally:
        driver.quit()
