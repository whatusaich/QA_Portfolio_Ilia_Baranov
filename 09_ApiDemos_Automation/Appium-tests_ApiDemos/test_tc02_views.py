from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Настройки подключения
caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "emulator-5554",  # название эмулятора (может отличаться у тебя)
    "app": "C:\\Users\\DELL\\Downloads\\ApiDemos-debug.apk"  # путь к APK
}

options = UiAutomator2Options().load_capabilities(caps)
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# TC-01: открыть Views
views = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views")
views.click()

# TC-02: открыть Buttons
buttons = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Buttons")
buttons.click()

time.sleep(2)
print("✅ TC-02: Экран 'Buttons' открыт, кнопки отображаются.")

driver.quit()
