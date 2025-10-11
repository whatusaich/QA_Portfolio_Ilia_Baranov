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
        time.sleep(0.5)

options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "emulator-5554",  # поменяй если нужно
    "app": r"C:\Users\DELL\Downloads\ApiDemos-debug.apk"
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    # 1) Открыть Views
    views = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(AppiumBy.ACCESSIBILITY_ID, "Views")
    )
    views.click()
    time.sleep(0.8)

    # 2) Доскроллить до Lists
    for _ in range(7):
        try:
            lists = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Lists")
            break
        except Exception:
            small_scroll(driver, times=1, percent=0.35)
    else:
        raise Exception("Не нашли пункт 'Lists'")

    lists.click()
    time.sleep(0.8)

    # 3) Доскроллить до "09. Array (Overlay)"
    target_text = "09. Array (Overlay)"
    for _ in range(7):
        try:
            array_overlay = driver.find_element(
                AppiumBy.XPATH, f'//android.widget.TextView[@text="{target_text}"]'
            )
            break
        except Exception:
            small_scroll(driver, times=1, percent=0.3)
    else:
        raise Exception(f"Не нашли пункт '{target_text}'")

    array_overlay.click()
    time.sleep(1.5)

    print("✅ TC-15 PASSED: Открылся экран '09. Array (Overlay)'")

except Exception as e:
    print(f"❌ TC-15 FAILED: {e}")

finally:
    driver.quit()