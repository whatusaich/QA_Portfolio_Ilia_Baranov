import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_enable_input():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    try:
        wait = WebDriverWait(driver, 15)

        # Находим кнопку (Enable или Disable)
        button = driver.find_element(By.CSS_SELECTOR, "#input-example button")

        # Если кнопка Enable → кликаем
        if button.text == "Enable":
            button.click()

        # Ждём сообщение
        message = wait.until(EC.visibility_of_element_located((By.ID, "message"))).text
        assert "It's enabled!" in message

        # Проверяем, что поле стало активным
        input_field = driver.find_element(By.CSS_SELECTOR, "#input-example input")
        assert input_field.is_enabled(), "Поле ввода должно быть разблокировано"
    finally:
        driver.quit()
