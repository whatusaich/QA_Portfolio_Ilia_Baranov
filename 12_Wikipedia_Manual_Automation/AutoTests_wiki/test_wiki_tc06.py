import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_wiki_language_switcher_exists():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

    try:
        wait = WebDriverWait(driver, 10)

        # Проверяем наличие переключателя языков
        lang_switcher = wait.until(
            EC.presence_of_element_located((By.ID, "p-lang-btn-checkbox"))
        )

        assert lang_switcher is not None, "Переключатель языка не найден в DOM"
        print("✅ TC-06 PASSED: Переключатель языка найден в DOM")

    finally:
        driver.quit()