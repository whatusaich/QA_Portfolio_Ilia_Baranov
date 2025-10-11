import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_uncheck_checkbox2():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    try:
        # Находим чекбоксы
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        checkbox2 = checkboxes[1]

        # Если чекбокс выбран — кликаем, чтобы снять
        if checkbox2.is_selected():
            checkbox2.click()

        # Проверка
        assert not checkbox2.is_selected(), "Чекбокс 2 должен быть снят"
    finally:
        driver.quit()





