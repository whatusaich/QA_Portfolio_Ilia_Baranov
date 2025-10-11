

import requests

BASE_URL = "https://pokeapi.co/api/v2"

def test_get_ability_by_id():
    """
    TC-03: Проверка получения способности по ID=1
    Ожидаемый результат: статус 200 и name = "stench"
    """
    resp = requests.get(f"{BASE_URL}/ability/1", timeout=15)

    # Проверяем статус-код
    assert resp.status_code == 200, f"Ожидали 200, получили {resp.status_code}"

    # Проверяем тело ответа
    data = resp.json()
    assert data.get("name") == "stench", (
        f'Ожидали name="stench", получили {data.get("name")}'
    )
