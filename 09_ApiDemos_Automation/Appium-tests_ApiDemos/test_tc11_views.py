import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройки драйвера
options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "emulator-5554",   # замени на свой
    "app": "C:\\Users\\DELL\\Downloads\\ApiDemos-debug.apk"
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    # Кликаем на "Views"
    views_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Views"))
    )
    views_button.click()
    time.sleep(1)

    # Скроллим до "Lists"
    while True:
        try:
            lists_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Lists")
            break
        except:
            driver.execute_script("mobile: scrollGesture", {
                "left": 100, "top": 500, "width": 500, "height": 1000,
                "direction": "down",
                "percent": 0.5
            })
    lists_button.click()
    time.sleep(1)

    # Скроллим до "05. Separators"
    while True:
        try:
            separators_button = driver.find_element(
                AppiumBy.XPATH, '//android.widget.TextView[@text="05. Separators"]'
            )
            break
        except:
            driver.execute_script("mobile: scrollGesture", {
                "left": 100, "top": 500, "width": 500, "height": 1000,
                "direction": "down",
                "percent": 0.3
            })

    separators_button.click()
    time.sleep(2)

    print("✅ TC-11 PASSED: Открыт экран 'Separators'")

except Exception as e:
    print("❌ TC-11 FAILED:", e)

finally:
    driver.quit()