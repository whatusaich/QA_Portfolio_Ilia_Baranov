import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_wiki_internal_reference_link():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://ru.wikipedia.org/wiki/Python")

    try:
        wait = WebDriverWait(driver, 15)

        # Находим первую сноску [1] в тексте статьи
        reference_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "sup.reference a"))
        )
        reference_link.click()

        # Проверяем, что произошёл переход в раздел "Примечания"
        current_url = driver.current_url
        assert "#cite_note" in current_url, "Переход по внутренней ссылке не сработал"

        print("✅ TC-12 PASSED: внутренняя ссылка корректно ведёт в раздел 'Примечания'")

    finally:
        driver.quit()