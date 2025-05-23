import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from configSetupTeardown import setup_teardown 

load_dotenv()
EMAIL = os.getenv("YOUTUBE_EMAIL")
SENHA = os.getenv("YOUTUBE_SENHA")

def test_videos_em_alta(setup_teardown):
    driver = setup_teardown
    driver.get("https://youtube.com")
    
    # Acessa a página de vídeos em alta
    videos_em_alta_button = driver.find_element(By.CSS_SELECTOR, "ytd-guide-entry-renderer.style-scope")
    videos_em_alta_button.click()
    
    time.sleep(3)
    
    # Verifica se a URL contém "/feed/trending"
    assert "/feed/trending" in driver.current_url
    print("✅ Acesso à página de vídeos em alta realizado com sucesso!")