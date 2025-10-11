import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

def test_file_upload():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/upload")

    try:
        wait = WebDriverWait(driver, 10)

        # Путь к файлу для загрузки
        file_path = r"C:\Users\DELL\test_file.txt"
        assert os.path.exists(file_path), f"Файл не найден: {file_path}"

        # Загружаем файл
        driver.find_element(By.ID, "file-upload").send_keys(file_path)
        driver.find_element(By.ID, "file-submit").click()

        # Проверяем успешную загрузку
        uploaded = wait.until(EC.visibility_of_element_located((By.ID, "uploaded-files"))).text
        assert "test_file.txt" in uploaded, f"Ожидали test_file.txt, получили {uploaded}"
    finally:
        driver.quit()
