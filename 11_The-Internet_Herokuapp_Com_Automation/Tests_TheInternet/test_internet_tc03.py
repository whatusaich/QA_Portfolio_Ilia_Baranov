import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_login_invalid_password():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")

    try:
        wait = WebDriverWait(driver, 10)

        # Вводим правильный логин и неверный пароль
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("wrongpass")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Проверяем сообщение об ошибке
        flash_text = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        ).text
        assert "Your password is invalid!" in flash_text

    finally:
        driver.quit()



