# test_tc17_slow_adapter.py
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait

def small_scroll(driver, times=1, percent=0.3):
    for _ in range(times):
        driver.execute_script("mobile: scrollGesture", {
            "left": 100, "top": 500, "width": 500, "height": 1000,
            "direction": "down",
            "percent": percent
        })
        time.sleep(0.4)

options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "emulator-5554",         # при необходимости поменяй
    "app": r"C:\Users\DELL\Downloads\ApiDemos-debug.apk"
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    # 1) Views
    views = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(AppiumBy.ACCESSIBILITY_ID, "Views")
    )
    views.click()
    time.sleep(0.6)

    # 2) Lists (скроллим малыми шагами, пока не найдём)
    for _ in range(8):
        try:
            lists = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Lists")
            break
        except Exception:
            small_scroll(driver, times=1, percent=0.35)
    else:
        raise Exception("Не нашли пункт 'Lists'")

    lists.click()
    time.sleep(0.6)

    # 3) 13. Slow Adapter (пробуем с номером, затем без номера — на всякий)
    target_xpath_numbered   = '//android.widget.TextView[@text="13. Slow Adapter"]'
    target_xpath_unnumbered = '//android.widget.TextView[@text="Slow Adapter"]'

    for _ in range(10):
        elems = driver.find_elements(AppiumBy.XPATH, target_xpath_numbered)
        if not elems:
            elems = driver.find_elements(AppiumBy.XPATH, target_xpath_unnumbered)
        if elems:
            slow_adapter = elems[0]
            break
        small_scroll(driver, times=1, percent=0.28)
    else:
        raise Exception("Не нашли пункт 'Slow Adapter' (с номером или без)")

    slow_adapter.click()
    time.sleep(0.8)

    # 4) Проверка, что список отрисовался и скроллится
    # Ищем сам ListView и его элементы
    list_view = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(AppiumBy.ID, "android:id/list")
    )

    # Должны быть видимые элементы (android:id/text1)
    items = driver.find_elements(AppiumBy.ID, "android:id/text1")
    assert len(items) > 0, "Элементы списка не найдены"

    # Скроллим внутри самого списка (по его прямоугольнику) — имитация «медленной подгрузки»
    rect = list_view.rect
    driver.execute_script("mobile: scrollGesture", {
        "left": rect["x"] + 10,
        "top": rect["y"] + 10,
        "width": rect["width"] - 20,
        "height": rect["height"] - 20,
        "direction": "down",
        "percent": 0.8
    })
    time.sleep(0.6)

    # После скролла снова должны быть элементы
    items_after = driver.find_elements(AppiumBy.ID, "android:id/text1")
    assert len(items_after) > 0, "После скролла элементы списка не видны"

    print("✅ TC-19 PASSED: 'Slow Adapter' открыт, список отображается и прокручивается")

except Exception as e:
    print(f"❌ TC-19 FAILED: {e}")

finally:
    driver.quit()