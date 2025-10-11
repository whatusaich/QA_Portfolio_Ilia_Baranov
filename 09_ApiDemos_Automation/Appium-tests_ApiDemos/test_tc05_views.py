from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

def start_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app = r"C:\Users\DELL\Downloads\ApiDemos-debug.apk"

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(5)
    return driver

# TC-05: Проверка ввода текста в TextField
def test_text_field(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()

    # скролл до Controls
    controls_menu = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Controls"));'
    )
    controls_menu.click()

    # открываем Light Theme
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Light Theme").click()

    # ввод текста
    text_field = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/edit")
    text_field.send_keys("Hello QA")

    # проверка
    entered = text_field.text
    assert entered == "Hello QA", f"Ожидали 'Hello QA', а получили '{entered}'"
    print("TC-05: PASS – текст введён корректно")

if __name__ == "__main__":
    driver = start_driver()
    try:
        test_text_field(driver)
    finally:
        driver.quit()