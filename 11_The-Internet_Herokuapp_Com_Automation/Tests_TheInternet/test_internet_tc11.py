import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_add_checkbox():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    try:
        wait = WebDriverWait(driver, 20)

        # Находим кнопку (Remove или Add)
        button = driver.find_element(By.CSS_SELECTOR, "#checkbox-example button")

        # Если Remove → удалим чекбокс
        if button.text == "Remove":
            button.click()
            wait.until(EC.text_to_be_present_in_element((By.ID, "message"), "It's gone!"))
            button = driver.find_element(By.CSS_SELECTOR, "#checkbox-example button")

        # Жмём Add
        button.click()

        # Ждём сообщение
        message = wait.until(EC.visibility_of_element_located((By.ID, "message"))).text
        assert "It's back!" in message

        # Ждём чекбокс по id="checkbox"
        checkbox = wait.until(EC.presence_of_element_located((By.ID, "checkbox")))
        assert checkbox.is_displayed(), "Чекбокс должен появиться"
    finally:
        driver.quit()





