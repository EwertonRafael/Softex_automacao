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

load_dotenv()
VIDEO = os.getenv("YOUTUBE_VIDEO_EXEMPLO")

@pytest.fixture
def setup_teardown():
    #setup
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(VIDEO) 
    driver.implicitly_wait(10)
    time.sleep(2)

    #teardown
    yield driver
    driver.quit()

def test_play_video_do_historico(setup_teardown):
    driver = setup_teardown #Recupera o driver

    #Mapear o botão play
    botao_play = driver.find_element(By.CSS_SELECTOR, ".ytp-play-button")
    botao_play.click()

    #Mapear o atributo para verificação do play
    atributo_play = botao_play.get_attribute("data-title-no-tooltip")
    time.sleep(5)

    assert atributo_play == "Pausa"
