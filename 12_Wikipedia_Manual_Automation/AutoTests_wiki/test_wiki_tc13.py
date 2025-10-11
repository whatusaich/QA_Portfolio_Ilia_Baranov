import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_wiki_external_link_python_org():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://ru.wikipedia.org/wiki/Python")

    try:
        wait = WebDriverWait(driver, 15)

        # Находим ссылку на официальный сайт Python в разделе "Ссылки"
        external_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.python.org/']"))
        )

        # Кликаем по ссылке (открывается новая вкладка)
        external_link.click()

        # Переключаемся на новую вкладку
        driver.switch_to.window(driver.window_handles[-1])

        # Проверяем, что мы перешли на сайт python.org
        assert "python.org" in driver.current_url, "Внешняя ссылка не открылась корректно"

        print("✅ TC-13 PASSED: Внешняя ссылка работает")

    finally:
        driver.quit()