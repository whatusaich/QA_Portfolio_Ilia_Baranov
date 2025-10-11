
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
    # 1. Находим и кликаем на "Views"
    views_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Views"))
    )
    views_button.click()
    time.sleep(1)

    # 2. Скроллим до "Lists"
    driver.execute_script("mobile: scrollGesture", {
        "left": 100, "top": 500, "width": 500, "height": 1000,
        "direction": "down",
        "percent": 1.5
    })

    lists_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Lists"))
    )
    lists_button.click()
    time.sleep(1)

    # 3. Делаем один скролл внутри экрана Lists
    driver.execute_script("mobile: scrollGesture", {
        "left": 100, "top": 500, "width": 500, "height": 1000,
        "direction": "down",
        "percent": 1.0
    })

    # 4. Теперь ищем "03. Cursor (Phones)"
    cursor_phones_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.TextView[@text="03. Cursor (Phones)"]')
        )
    )
    cursor_phones_button.click()
    time.sleep(2)

    print("✅ TC-09 PASSED: Открыт экран 'Cursor (Phones)'")

except Exception as e:
    print("❌ TC-09 FAILED:", e)

finally:
    driver.quit()