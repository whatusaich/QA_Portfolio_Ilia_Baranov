import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

def test_select_option2():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/dropdown")

    try:
        dropdown = Select(driver.find_element(By.ID, "dropdown"))
        dropdown.select_by_visible_text("Option 2")

        selected = dropdown.first_selected_option.text
        assert selected == "Option 2", f"Ожидали 'Option 2', получили '{selected}'"
    finally:
        driver.quit()






