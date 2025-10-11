import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_wiki_open_language_menu():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

    try:
        wait = WebDriverWait(driver, 15)

        # Ждём label, связанный с чекбоксом переключателя языков
        label = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='p-lang-btn-checkbox']"))
        )

        # Кликаем через JS (надёжнее, чем .click())
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", label)
        driver.execute_script("arguments[0].click();", label)

        # Проверяем, что aria-expanded у чекбокса стало "true"
        checkbox = driver.find_element(By.ID, "p-lang-btn-checkbox")
        is_open = checkbox.get_attribute("aria-expanded") == "true"

        assert is_open, "Меню языков не открылось"
        print("✅ TC-08-STEP1 PASSED: Меню языков успешно открылось")

        # Держим браузер открытым 10 секунд
        time.sleep(10)

    finally:
        driver.quit()