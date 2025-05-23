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


def test_shorts(setup_teardown):
    driver = setup_teardown
    driver.get("https://youtube.com")
    shorts_button = driver.find_element(By.CSS_SELECTOR, '#endpoint')
    shorts_button = driver.find_element(By.ID,"header")
    


    shorts_button.click()
    time.sleep(3)
    
    # Verifica se a URL contém "/shorts"
    assert "/shorts" in driver.current_url
    print("✅ Acesso à página de Shorts realizado com sucesso!")


