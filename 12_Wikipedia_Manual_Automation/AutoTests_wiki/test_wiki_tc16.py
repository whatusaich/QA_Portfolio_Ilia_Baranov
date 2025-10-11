import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_wiki_mobile_responsive():
    # Настройки для эмулятора
    capabilities = {
        "platformName": "Android",
        "platformVersion": "11.0",  # замени на версию своего эмулятора
        "deviceName": "Android Emulator",
        "browserName": "Chrome",
        "automationName": "UiAutomator2"
    }

    # Подключение к Appium 3.x (новый синтаксис)
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=None,
        desired_capabilities=None,
        keep_alive=True,
        direct_connection=True,
        strict_ssl=False,
        **capabilities
    )

    try:
        driver.get("https://ru.m.wikipedia.org/wiki/Python")

        wait = WebDriverWait(driver, 20)

        # Ждём появления кнопки поиска
        search_button = wait.until(
            EC.element_to_be_clickable((By.ID, "searchIcon"))
        )
        search_button.click()

        # Проверяем, что появилось поле поиска
        search_input = wait.until(
            EC.presence_of_element_located((By.NAME, "search"))
        )
        assert search_input.is_displayed(), "Поле поиска не открылось"

        print("✅ TC-16 PASSED: Мобильная версия показывает поиск")

    finally:
        driver.quit()