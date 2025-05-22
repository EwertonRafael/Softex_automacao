
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import pytest
import time

load_dotenv()
EMAIL = os.getenv("YOUTUBE_EMAIL")
SENHA = os.getenv("YOUTUBE_SENHA")

@pytest.fixture
def setup_teardown():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dpt%26next%3D%252F%2540softexpe4294&ec=65620&hl=pt-BR&ifkv=ASKV5Mjf8JtHp9rmGETRb-oHM3jQxcCgJUDQ3LIXNXGcErDT3X6B2AbOo7XcBbRkW0XcdqcPIjXNpw&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-250833250%3A1747877017702189")
    driver.implicitly_wait(10)
    time.sleep(2)
    yield driver
    driver.quit()

def test_login_bem_sucedido(setup_teardown):
    driver = setup_teardown
    wait = WebDriverWait(driver, 20)
    email_input = driver.find_element(By.CSS_SELECTOR, "#identifierId")
    email_input.send_keys(EMAIL)
    botao_avancar_email = driver.find_element(By.CSS_SELECTOR, "#identifierNext")
    botao_avancar_email.click()
    senha_input = driver.find_element(By.NAME, "Passwd")
    senha_input.send_keys(SENHA)
    botao_entrar = driver.find_element(By.CSS_SELECTOR, "#passwordNext")
    botao_entrar.click()
    time.sleep(10)

    wait.until(EC.url_contains("youtube"))
    assert "youtube" in driver.current_url.lower()
    print("✅ Login realizado com sucesso!")