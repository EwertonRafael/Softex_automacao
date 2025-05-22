import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from configSetupTeardown import setup_teardown

def test_busca(setup_teardown):
  driver = setup_teardown
  driver.get("https://youtube.com")
  input_busca = driver.find_element(By.NAME, "search_query")
  input_busca.send_keys("curso de python")
  resultados = driver.find_element(By.CSS_SELECTOR, 'button[title="Pesquisar"]').click()
  time.sleep(3)
  