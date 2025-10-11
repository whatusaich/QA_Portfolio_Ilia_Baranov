import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_remove_checkbox():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    try:
        wait = WebDriverWait(driver, 10)

        # Нажимаем Remove
        driver.find_element(By.CSS_SELECTOR, "button[onclick='swapCheckbox()']").click()

        # Ждём сообщение
        message = wait.until(
            EC.visibility_of_element_located((By.ID, "message"))
        ).text
        assert "It's gone!" in message

        # Проверяем, что чекбокса больше нет
        checkbox_area = driver.find_element(By.ID, "checkbox-example").text
        assert "checkbox" not in checkbox_area.lower(), "Чекбокс не должен отображаться"
    finally:
        driver.quit()

