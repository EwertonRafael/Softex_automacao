import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture
def setup_teardown():
  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service)
  driver.get("https://youtube.com")
  driver.implicitly_wait(10)
  time.sleep(2)
  yield driver
  driver.quit()