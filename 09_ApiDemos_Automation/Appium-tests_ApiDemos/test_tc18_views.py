import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait

options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "emulator-5554",  # замени на свой
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

    # Скроллим до Lists
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

    # Скроллим до Transcript
    driver.execute_script("mobile: scrollGesture", {
        "left": 100, "top": 500, "width": 500, "height": 1000,
        "direction": "down",
        "percent": 1.0
    })
    transcript_button = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="12. Transcript"]')
    )
    transcript_button.click()
    time.sleep(2)

    print("✅ TC-18 PASSED: Экран 'Transcript' открыт")

except Exception as e:
    print("❌ TC-18 FAILED:", e)

finally:
    driver.quit()