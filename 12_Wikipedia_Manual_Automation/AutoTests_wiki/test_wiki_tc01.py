import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_wiki_search_python():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://en.wikipedia.org/")  # главная страница

    try:
        wait = WebDriverWait(driver, 15)

        # 1) Кликаем по иконке поиска (лупа)
        search_toggle = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.search-toggle"))
        )
        search_toggle.click()

        # 2) Ждём появления поля ввода
        search_input = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input.cdx-text-input__input[name='search']")
            )
        )
        search_input.send_keys("Python")
        search_input.send_keys(Keys.ENTER)

        # 3) Проверяем заголовок
        heading = wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))
        text = heading.text.strip()

        if text != "Python (programming language)":
            # если попали на дизамбиг
            target_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@title='Python (programming language)']"))
            )
            target_link.click()
            heading = wait.until(EC.visibility_of_element_located((By.ID, "firstHeading")))
            text = heading.text.strip()

        assert text == "Python (programming language)", f"Ожидали 'Python (programming language)', получили: '{text}'"
        print("✅ TC-01 PASSED: Открылась статья 'Python (programming language)'")

    finally:
        driver.quit()