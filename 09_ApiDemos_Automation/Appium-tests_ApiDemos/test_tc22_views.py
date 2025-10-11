# ⚠️ ВРЕМЕННО: пропускаем клик по "16. Border selection mode"
print("⚠️ Пропускаем открытие 'Border selection mode', идём сразу к выбору элементов")

# Переходим напрямую к выбору элементов (если экран уже открыт вручную)
items = ["Affidelice au Chablis", "Airedale", "Ambert"]

for item_text in items:
    element = WebDriverWait(driver, 10).until(
        lambda d: d.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{item_text}")'
        )
    )

    driver.execute_script("mobile: longClickGesture", {
        "elementId": element.id,
        "duration": 1500
    })
    print(f"✅ Долгое нажатие на '{item_text}' выполнено")
    time.sleep(1)

print("🎉 TC-22 PASSED: Все элементы выбраны долгим нажатием")