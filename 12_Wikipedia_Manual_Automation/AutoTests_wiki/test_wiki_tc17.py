import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_wiki_edit_history_section():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://ru.wikipedia.org/wiki/Python")

    try:
        wait = WebDriverWait(driver, 20)

        # 1) Находим заголовок "История" и скроллим к нему
        history_header = wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='mw-headline' and normalize-space()='История']"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", history_header)

        # 2) Ищем ссылку 'править' у ЭТОГО заголовка (это соседний span.mw-editsection)
        edit_link = wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "(//span[@class='mw-headline' and normalize-space()='История']"
                "/following-sibling::span[contains(@id301415451 (@class),'mw-editsection')]//a"
                "[contains(normalize-space(.), 'править')])[1]"
            ))
        )

        # 3) На всякий — скрываем возможные баннеры, чтобы клик не перехватывался
        driver.execute_script("""
            (function(){
                const sel = ['#centralNotice', '.central-notice', '.banner', '#frb-inline', '.ext-dismissable-notice'];
                sel.forEach(s => document.querySelectorAll(s).forEach(el => el.style.display='none'));
            })();
        """)

        # 4) Скролл к самой ссылке и клик через JS (устойчивее)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", edit_link)
        driver.execute_script("arguments[0].click();", edit_link)

        # 5) Подтверждаем, что открылась страница редактирования раздела
        wait.until(lambda d: ("section=" in d.current_url) and ("action=edit" in d.current_url or "veaction=edit" in d.current_url))
        assert "section=" in driver.current_url and ("action=edit" in driver.current_url or "veaction=edit" in driver.current_url), \
            "Редактор раздела не открылся"

        print("✅ TC-17 PASSED: Кнопка «править» у раздела «История» открывает редактор")

    finally:
        driver.quit()