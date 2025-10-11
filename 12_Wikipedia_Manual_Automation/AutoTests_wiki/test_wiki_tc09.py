import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_wiki_toc_exists():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://ru.wikipedia.org/wiki/Python")

    try:
        wait = WebDriverWait(driver, 10)

        # Проверяем, что оглавление существует
        toc = wait.until(EC.presence_of_element_located((By.ID, "toc")))

        assert toc.is_displayed(), "Оглавление не отображается"
        print("✅ TC-09 PASSED: Оглавление найдено")
    finally:
        driver.quit()