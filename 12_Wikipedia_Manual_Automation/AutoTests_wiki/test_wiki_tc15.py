import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_wiki_revision_navigation_diff():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://ru.wikipedia.org/w/index.php?title=Python&action=history")

    try:
        wait = WebDriverWait(driver, 15)

        # Дождаться списка правок (страница истории загрузилась)
        wait.until(EC.presence_of_element_located((By.ID, "pagehistory")))

        # Кликаем по ССЫЛКЕ НА DIFF: "пред." (а не по пагинации "Предыдущая")
        # Берём первую доступную ссылку "пред."
        prev_diff_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space(text())='пред.'])[1]"))
        )
        prev_diff_link.click()

        # Проверяем, что открылась страница сравнения ревизий
        wait.until(lambda d: "diff=" in d.current_url and "oldid=" in d.current_url)

        assert "diff=" in driver.current_url and "oldid=" in driver.current_url, \
            f"Ожидали diff/oldid в URL, получили: {driver.current_url}"

        print("✅ TC-15 PASSED: Переход к сравнению ревизий через ссылку «пред.» работает")

    finally:
        driver.quit()