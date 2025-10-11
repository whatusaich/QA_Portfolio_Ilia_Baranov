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
    # Находим и кликаем на "Views"
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
                "percent": 0.5  # маленький шаг
            })
    lists_button.click()
    time.sleep(1)

    # Скроллим до "04. ListAdapter"
    while True:
        try:
            list_adapter_button = driver.find_element(
                AppiumBy.XPATH, '//android.widget.TextView[@text="04. ListAdapter"]'
            )
            break
        except:
            driver.execute_script("mobile: scrollGesture", {
                "left": 100, "top": 500, "width": 500, "height": 1000,
                "direction": "down",
                "percent": 0.3  # очень маленький шаг
            })

    list_adapter_button.click()
    time.sleep(2)

    print("✅ TC-10 PASSED: Открыт экран 'ListAdapter'")

except Exception as e:
    print("❌ TC-10 FAILED:", e)

finally:
    driver.quit()