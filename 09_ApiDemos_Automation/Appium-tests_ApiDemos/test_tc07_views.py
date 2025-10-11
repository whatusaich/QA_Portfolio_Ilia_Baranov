import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait

# Настройки драйвера
options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "emulator-5554",   # замени на свой
    "app": "C:\\Users\\DELL\\Downloads\\ApiDemos-debug.apk"
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    # Переход в Views
    views_button = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(AppiumBy.ACCESSIBILITY_ID, "Views")
    )
    views_button.click()
    time.sleep(1)

    # Скролл до Lists
    driver.execute_script("mobile: scrollGesture", {
        "left": 100, "top": 500, "width": 500, "height": 1000,
        "direction": "down",
        "percent": 1.0
    })

    lists_button = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(AppiumBy.ACCESSIBILITY_ID, "Lists")
    )
    lists_button.click()
    time.sleep(1)

    # Клик по "01. Array"
    array_button = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="01. Array"]')
    )
    array_button.click()
    time.sleep(2)

    print("✅ TC07-Array PASSED: Экран '01. Array' открыт")

except Exception as e:
    print("❌ TC07-Array FAILED:", e)

finally:
    driver.quit()