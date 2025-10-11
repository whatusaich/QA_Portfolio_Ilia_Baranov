import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_wiki_revision_history():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://ru.wikipedia.org/wiki/Python")

    try:
        wait = WebDriverWait(driver, 15)

        # Находим вкладку "История"
        history_tab = wait.until(
            EC.element_to_be_clickable((By.ID, "ca-history"))
        )
        history_tab.click()

        # Проверяем, что мы на странице истории правок
        assert "action=history" in driver.current_url, "Страница истории правок не открылась"

        print("✅ TC-14 PASSED: История правок доступна")

    finally:
        driver.quit()