import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

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
        lambda d: d.find_element(AppiumBy.ACCESSIBILITY_ID, "Views")
    )
    views_button.click()
    time.sleep(1)

    # Пробуем найти "Lists", если нет — скроллим пока не появится
    found = False
    for i in range(5):  # максимум 5 скроллов, чтобы не уйти в бесконечный цикл
        try:
            lists_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Lists")
            found = True
            break
        except:
            driver.execute_script("mobile: scrollGesture", {
                "left": 100, "top": 500, "width": 500, "height": 1000,
                "direction": "down",
                "percent": 1.0
            })
            time.sleep(1)

    if not found:
        raise Exception("Кнопка 'Lists' не найдена даже после скроллинга")

    lists_button.click()
    time.sleep(1)

    # Нажимаем на "02. Cursor (People)"
    cursor_people_button = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="02. Cursor (People)"]')
    )
    cursor_people_button.click()
    time.sleep(2)

    print("✅ TC-08 PASSED: Открыт экран 'Cursor (People)'")

except Exception as e:
    print("❌ TC-08 FAILED:", e)

finally:
    driver.quit()