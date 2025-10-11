import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_check_checkbox1():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    try:
        # Находим чекбоксы
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        checkbox1 = checkboxes[0]

        # Если чекбокс не выбран — кликаем
        if not checkbox1.is_selected():
            checkbox1.click()

        # Проверка
        assert checkbox1.is_selected(), "Чекбокс 1 должен быть отмечен"
    finally:
        driver.quit()




