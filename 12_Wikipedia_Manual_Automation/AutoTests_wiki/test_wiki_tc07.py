import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_wiki_language_switcher_opens():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

    try:
        wait = WebDriverWait(driver, 15)

        # 1) Находим чекбокс и связанный label
        checkbox = wait.until(EC.presence_of_element_located((By.ID, "p-lang-btn-checkbox")))
        label = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='p-lang-btn-checkbox']")))

        # 2) Скролл + JS-клик по label (обходит перехват клика и перекрытия)
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", label)
        driver.execute_script("arguments[0].click();", label)

        # 3) Ждём, что меню действительно открылось (любой из трёх признаков)
        def menu_opened(d):
            try:
                if d.find_element(By.ID, "p-lang-btn-checkbox").get_attribute("aria-expanded") == "true":
                    return True
            except Exception:
                pass
            try:
                m = d.find_element(By.CSS_SELECTOR, ".uls-menu")
                if m.is_displayed():
                    return True
            except Exception:
                pass
            try:
                box = d.find_element(By.CSS_SELECTOR, "#p-lang .vector-menu-content, #p-lang .vector-menu-content-list")
                if box.is_displayed():
                    return True
            except Exception:
                pass
            return False

        wait.until(menu_opened)
        print("✅ TC-07 PASSED: Список языков открылся")

    finally:
        driver.quit()