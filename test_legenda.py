import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture 
def setup_teardown():
    # Setup
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.youtube.com/watch?v=JsXoTHyy6j0&t=20s")
    driver.set_window_position(2000, 0)
    driver.implicitly_wait(10)
    # time.sleep(2)
    # Teardown
    yield driver
    driver.quit()

def test_ativa_legenda(setup_teardown):
    driver = setup_teardown
    time.sleep(5)

    botao_play = driver.find_element(By.CSS_SELECTOR, ".ytp-play-button")
    icone_legenda = driver.find_element(By.CSS_SELECTOR, ".ytp-subtitles-button")

    time.sleep(5)

    botao_play.click()

    icone_legenda.click()
    botao_play.click()

    time.sleep(6)
    atributo_legenda = icone_legenda.get_attribute("aria-pressed")

    assert atributo_legenda == "true"

