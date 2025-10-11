import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

def test_file_upload_without_file():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/upload")

    try:
        # Жмём Upload без выбора файла
        driver.find_element(By.ID, "file-submit").click()

        # Проверяем отсутствие элемента uploaded-files
        try:
            uploaded = driver.find_element(By.ID, "uploaded-files")
            assert uploaded.text.strip() == "", "Файл не должен отображаться"
        except NoSuchElementException:
            # Если элемента нет — это тоже ожидаемое поведение
            pass
    finally:
        driver.quit()
