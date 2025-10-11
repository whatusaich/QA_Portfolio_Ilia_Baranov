import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

# Настройки драйвера
options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "emulator-5554",   # замени на свой
    "app": "C:\\Users\\DELL\\Downloads\\ApiDemos-debug.apk"
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    # Открываем Views
    views_button = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(AppiumBy.ACCESSIBILITY_ID, "Views")
    )
    views_button.click()
    time.sleep(1)

    # Скроллим до Lists
    lists_button = None
    for _ in range(5):
        try:
            lists_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Lists")
            break
        except NoSuchElementException:
            driver.execute_script("mobile: scrollGesture", {
                "left": 100, "top": 500, "width": 500, "height": 1000,
                "direction": "down", "percent": 0.8
            })
            time.sleep(1)

    if not lists_button:
        raise Exception("Кнопка 'Lists' не найдена")
    lists_button.click()
    time.sleep(1)

    # Скроллим до "15. Selection Mode"
    selection_mode = None
    for _ in range(5):
        try:
            selection_mode = driver.find_element(
                AppiumBy.XPATH,
                '//android.widget.TextView[@content-desc="15. Selection Mode"]'
            )
            break
        except NoSuchElementException:
            driver.execute_script("mobile: scrollGesture", {
                "left": 100, "top": 500, "width": 500, "height": 1000,
                "direction": "down", "percent": 0.8
            })
            time.sleep(1)

    if not selection_mode:
        raise Exception("Кнопка 'Selection Mode' не найдена")
    selection_mode.click()
    time.sleep(1)

    # Находим Abondance
    abondance_item = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(
            AppiumBy.XPATH,
            '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Abondance"]'
        )
    )

    # Долгое нажатие (long press)
    driver.execute_script("mobile: longClickGesture", {
        "elementId": abondance_item.id,
        "duration": 1500   # удержание ~1.5 сек
    })
    print("✅ Долгое нажатие на 'Abondance' выполнено")
    time.sleep(1)

    # Находим Alverca
    alverca_item = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(
            AppiumBy.XPATH,
            '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Alverca"]'
        )
    )

    driver.execute_script("mobile: longClickGesture", {
        "elementId": alverca_item.id,
        "duration": 1500
    })
    print("✅ Долгое нажатие на 'Alverca' выполнено")

    time.sleep(1)
    print("🎉 TC-21 PASSED: Оба элемента выбраны долгим нажатием")

except Exception as e:
    print("❌ TC-21 FAILED:", e)

finally:
    driver.quit()