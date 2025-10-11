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
    # Находим и кликаем на "Views"
    views_button = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(AppiumBy.ACCESSIBILITY_ID, "Views")
    )
    views_button.click()
    time.sleep(1)

    # Скроллим до "Lists" только пока не найдено
    lists_button = None
    for _ in range(5):  # максимум 5 попыток
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

    # Скроллим до "14. Efficient Adapter"
    efficient_adapter = None
    for _ in range(5):
        try:
            efficient_adapter = driver.find_element(
                AppiumBy.XPATH,
                '//android.widget.TextView[@text="14. Efficient Adapter"]'
            )
            break
        except NoSuchElementException:
            driver.execute_script("mobile: scrollGesture", {
                "left": 100, "top": 500, "width": 500, "height": 1000,
                "direction": "down", "percent": 0.8
            })
            time.sleep(1)

    if not efficient_adapter:
        raise Exception("Кнопка 'Efficient Adapter' не найдена")
    efficient_adapter.click()
    time.sleep(2)

    print("✅ TC-20 PASSED: Открылся экран 'Efficient Adapter' со списком элементов")

except Exception as e:
    print("❌ TC-20 FAILED:", e)

finally:
    driver.quit()