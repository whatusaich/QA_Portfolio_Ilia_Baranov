import requests

BASE_URL = "https://pokeapi.co/api/v2"

def test_get_type_by_id():
    """
    TC-04: Проверка получения типа покемона по ID=3
    Ожидаемый результат: статус 200, name="flying" и список покемонов не пуст
    """
    resp = requests.get(f"{BASE_URL}/type/3", timeout=15)

    # Проверяем статус-код
    assert resp.status_code == 200, f"Ожидали 200, получили {resp.status_code}"

    # Проверяем тело ответа
    data = resp.json()
    assert data.get("name") == "flying", (
        f'Ожидали name=\"flying\", получили {data.get("name")}'
    )
    assert "pokemon" in data, "В ответе нет ключа 'pokemon'"
    assert len(data["pokemon"]) > 0, "Список покемонов пуст"
