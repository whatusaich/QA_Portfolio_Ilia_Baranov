import requests

BASE_URL = "https://pokeapi.co/api/v2"

def test_get_all_types():
    """
    TC-10: Проверка запроса списка всех типов
    Ожидаемый результат: статус 200 и список типов не пуст
    """
    resp = requests.get(f"{BASE_URL}/type", timeout=15)

    # Проверяем статус-код
    assert resp.status_code == 200, f"Ожидали 200, получили {resp.status_code}"

    # Проверяем тело ответа
    data = resp.json()
    assert "results" in data, "В ответе нет ключа 'results'"
    assert len(data["results"]) > 0, "Список типов пуст"
