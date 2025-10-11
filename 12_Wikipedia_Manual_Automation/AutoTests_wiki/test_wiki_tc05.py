import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_wiki_autocomplete_python_programming_language():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://en.wikipedia.org/wiki/Main_Page")

    try:
        wait = WebDriverWait(driver, 10)

        # 1) Кликаем по иконке поиска
        search_toggle = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.search-toggle"))
        )
        search_toggle.click()

        # 2) Вводим "Python"
        search_input = wait.until(
            EC.element_to_be_clickable((By.NAME, "search"))
        )
        search_input.send_keys("Python")

        # 3) Ждём именно подсказку с текстом "Python (programming language)"
        suggestion = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//span[@class='cdx-menu-item__text__label']/bdi[text()='Python (programming language)']"
            ))
        )

        # 4) Поднимаемся на <a> и кликаем
        parent_link = suggestion.find_element(By.XPATH, "./ancestor::a")
        driver.execute_script("arguments[0].click();", parent_link)

        # 5) Проверяем заголовок страницы
        heading = wait.until(EC.presence_of_element_located((By.ID, "firstHeading")))
        page_title = heading.text.strip()

        assert page_title == "Python (programming language)", (
            f"Ожидали 'Python (programming language)', но получили '{page_title}'"
        )
        print("✅ TC-05 PASSED: Из автодополнения выбрана 'Python (programming language)'")

    finally:
        driver.quit()