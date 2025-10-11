import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_login_success():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")

    try:
        wait = WebDriverWait(driver, 10)

        # Вводим валидные креды и логинимся
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Ждём и проверяем уведомление об успехе
        flash_text = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        ).text
        assert "You logged into a secure area!" in flash_text

        # Дополнительно проверим, что перешли на защищённую страницу
        assert "/secure" in driver.current_url
    finally:
        driver.quit()

