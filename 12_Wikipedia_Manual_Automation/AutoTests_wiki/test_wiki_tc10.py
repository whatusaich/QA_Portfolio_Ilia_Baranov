import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import unquote
from webdriver_manager.chrome import ChromeDriverManager

def test_wiki_toc_history_section():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://ru.wikipedia.org/wiki/Python")

    try:
        wait = WebDriverWait(driver, 15)

        # Находим пункт "История" в оглавлении
        history_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='toctext' and text()='История']"))
        )

        # Кликаем по пункту
        history_link.click()

        # Получаем URL и декодируем
        current_url = unquote(driver.current_url)

        assert "#История" in current_url, f"Переход не сработал, текущий URL: {current_url}"
        print("✅ TC-10 PASSED: Переход к разделу 'История' работает корректно")

    finally:
        driver.quit()