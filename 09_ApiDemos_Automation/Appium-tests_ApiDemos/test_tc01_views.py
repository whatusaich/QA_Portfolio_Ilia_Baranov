from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# Desired capabilities
caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "emulator-5554",  # название твоего эмулятора
    "app": "C:\\Users\\DELL\\Downloads\\ApiDemos-debug.apk"  # путь к apk
}

# Создаем options и передаем туда capabilities
options = UiAutomator2Options().load_capabilities(caps)

# Запускаем сессию
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Тест-кейс 01: открыть Views
views = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views")
views.click()

print("TC-01: Экран 'Views' успешно открыт!")

driver.quit()

