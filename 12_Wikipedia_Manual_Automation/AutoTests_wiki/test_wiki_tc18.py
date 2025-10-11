import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_wiki_random_article():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://ru.wikipedia.org/wiki/Python")

    try:
        wait = WebDriverWait(driver, 20)

        # Ждём кнопку "Случайная статья"
        random_link = wait.until(
            EC.element_to_be_clickable((By.ID, "n-randompage"))
        )

        # Кликаем по кнопке
        random_link.click()

        # Проверяем, что мы перешли на новый URL
        assert "wiki/" in driver.current_url, "Не удалось открыть случайную статью"
        assert "Python" not in driver.current_url, "Остались на той же странице"

        print("✅ TC-18 PASSED: Случайная статья открывается")

    finally:
        driver.quit()