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

# TC-04: Проверка открытия меню Controls
def test_controls(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()

    # находим Controls (может быть ниже списка → скролл)
    controls_menu = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Controls"));'
    )
    controls_menu.click()

    # проверяем наличие Light Theme
    light_theme = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Light Theme")
    assert light_theme.is_displayed(), "Light Theme не найден"
    print("TC-04: PASS – Controls открыт, Light Theme доступен")

if __name__ == "__main__":
    driver = start_driver()
    try:
        test_controls(driver)
    finally:
        driver.quit()