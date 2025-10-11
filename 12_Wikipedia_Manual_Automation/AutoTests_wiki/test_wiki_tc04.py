import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_wiki_autocomplete():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://en.wikipedia.org/wiki/Main_Page")

    try:
        wait = WebDriverWait(driver, 10)

        # Кликаем по иконке поиска
        search_toggle = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.search-toggle")))
        search_toggle.click()

        # Находим поле поиска и вводим часть слова
        search_input = wait.until(EC.element_to_be_clickable((By.NAME, "search")))
        search_input.send_keys("Pyth")

        # Ждём появления выпадающего списка
        suggestion = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(., 'Python (programming language)')]")
            )
        )

        # Кликаем на нужную подсказку
        suggestion.click()

        # Проверяем, что открылась нужная страница
        heading = wait.until(EC.presence_of_element_located((By.ID, "firstHeading")))
        assert heading.text == "Python (programming language)", "Открылась не та страница"

        print("✅ TC-04 PASSED: Автодополнение работает корректно")

    finally:
        driver.quit()