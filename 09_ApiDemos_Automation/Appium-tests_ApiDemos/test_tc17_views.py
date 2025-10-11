import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait

# Настройки драйвера
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

    # Скролл до Multiple choice list
    driver.execute_script("mobile: scrollGesture", {
        "left": 100, "top": 500, "width": 500, "height": 1000,
        "direction": "down",
        "percent": 1.0
    })

    multiple_choice_button = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="11. Multiple choice list"]')
    )
    multiple_choice_button.click()
    time.sleep(1)

    # Отмечаем "Adventure" и "Drama"
    adventure_item = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Adventure"]')
    )
    drama_item = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Drama"]')
    )

    adventure_item.click()
    drama_item.click()
    time.sleep(2)

    print("✅ TC-17 PASSED: Элементы 'Adventure' и 'Drama' выбраны в Multiple choice list")

except Exception as e:
    print("❌ TC-17 FAILED:", e)

finally:
    driver.quit()