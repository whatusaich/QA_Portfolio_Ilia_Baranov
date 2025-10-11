import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options

desired_caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "emulator-5554",
    "platformVersion": "15.0",
    "app": "C:\\Users\\DELL\\Downloads\\ApiDemos-debug.apk"
}

driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4723",
    options=UiAutomator2Options().load_capabilities(desired_caps)
)

try:
    # Ожидаем появления меню "Views"
    views = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Views"))
    )
    views.click()

    # Используем UiScrollable для поиска элемента "Lists"
    lists = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("Lists"));'
    )
    lists.click()

    print("TC-06 PASSED: Экран Lists успешно открыт")

except Exception as e:
    print("TC-06 FAILED:", str(e))

finally:
    time.sleep(3)
    driver.quit()