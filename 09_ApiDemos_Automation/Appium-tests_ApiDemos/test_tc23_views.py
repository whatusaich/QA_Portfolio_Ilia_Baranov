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
    # 1. Открываем Views
    views_button = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(AppiumBy.ACCESSIBILITY_ID, "Views")
    )
    views_button.click()
    time.sleep(1)

    # 2. Скроллим до Lists
    lists_button = None
    for _ in range(7):
        try:
            lists_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Lists")
            break
        except NoSuchElementException:
            driver.execute_script("mobile: scrollGesture", {
                "left": 100, "top": 500, "width": 500, "height": 1000,
                "direction": "down", "percent": 0.9
            })
            time.sleep(0.5)

    if not lists_button:
        raise Exception("❌ Не удалось найти пункт 'Lists'")
    lists_button.click()
    time.sleep(1)

    # 3. Скроллим до "17. Activate items"
    activate_items = None
    for _ in range(10):
        try:
            activate_items = driver.find_element(
                AppiumBy.XPATH,
                '//android.widget.TextView[@content-desc="17. Activate items"]'
            )
            activate_items.click()
            print("✅ Открыт экран 'Activate items'")
            break
        except NoSuchElementException:
            driver.execute_script("mobile: scrollGesture", {
                "left": 100, "top": 500, "width": 500, "height": 1000,
                "direction": "down", "percent": 0.9
            })
            time.sleep(0.5)

    if not activate_items:
        raise Exception("❌ Не удалось найти '17. Activate items'")

    time.sleep(1)

    # 4. Конкретные элементы для активации
    target_items = ["Abertam", "Ambert"]

    for item_text in target_items:
        # Скроллим пока не найдём элемент
        element = None
        for _ in range(10):
            try:
                element = driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().text("{item_text}")'
                )
                break
            except NoSuchElementException:
                driver.execute_script("mobile: scrollGesture", {
                    "left": 100, "top": 500, "width": 500, "height": 1000,
                    "direction": "down", "percent": 0.9
                })
                time.sleep(0.5)

        if not element:
            raise Exception(f"❌ Элемент '{item_text}' не найден")

        # Долгое нажатие
        driver.execute_script("mobile: longClickGesture", {
            "elementId": element.id,
            "duration": 1200
        })

        # Проверка атрибутов
        state = element.get_attribute("checked") or element.get_attribute("activated")
        print(f"👉 Элемент '{item_text}', состояние={state}")

        assert state == "true", f"❌ Элемент '{item_text}' не активирован"
        print(f"✅ Элемент '{item_text}' успешно активирован")
        time.sleep(1)

    print("🎉 TC-23 PASSED: Элементы 'Abertam' и 'Ambert' активированы")

except Exception as e:
    print("❌ TC-23 FAILED:", e)
    try:
        driver.save_screenshot("tc22_fail.png")
        print("🖼 Скриншот сохранён: tc22_fail.png")
    except:
        pass

finally:
    driver.quit()