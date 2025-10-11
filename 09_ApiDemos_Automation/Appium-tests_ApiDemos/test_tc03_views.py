from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

def start_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"   # замени на своё устройство
    options.app = r"C:\Users\DELL\Downloads\ApiDemos-debug.apk"

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(5)
    return driver

# TC-03: Проверка работы Toggle Button
def test_toggle_button(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Buttons").click()

    toggle = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/button_toggle")
    initial_state = toggle.text
    toggle.click()
    new_state = toggle.text

    assert initial_state != new_state, "Состояние кнопки не изменилось"
    print(f"TC-03: PASS – Toggle изменился {initial_state} → {new_state}")

if __name__ == "__main__":
    driver = start_driver()
    try:
        test_toggle_button(driver)
    finally:
        driver.quit()