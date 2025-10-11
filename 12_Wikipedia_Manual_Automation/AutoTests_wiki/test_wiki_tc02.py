import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_wiki_search_nonexistent():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://en.wikipedia.org/")  # главная страница

    try:
        wait = WebDriverWait(driver, 15)

        # 1) Кликаем по иконке поиска (лупа)
        search_toggle = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.search-toggle"))
        )
        search_toggle.click()

        # 2) Вводим несуществующий запрос
        search_input = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input.cdx-text-input__input[name='search']")
            )
        )
        search_input.send_keys("Asldkfjweoi")
        search_input.send_keys(Keys.ENTER)

        # 3) Проверяем наличие текста об отсутствии результатов
        no_results = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[contains(text(), 'There were no results matching the query')]")
            )
        )

        assert "There were no results matching the query" in no_results.text
        print("✅ TC-02 PASSED: Сообщение об отсутствии результатов отображается")

    finally:
        driver.quit()