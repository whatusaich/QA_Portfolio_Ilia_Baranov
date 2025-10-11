import requests

BASE_URL = "https://pokeapi.co/api/v2"

def test_get_invalid_pokemon_id():
    """
    TC-06: Проверка запроса покемона с очень большим ID
    Ожидаемый результат: статус 404
    """
    resp = requests.get(f"{BASE_URL}/pokemon/999999", timeout=15)

    # Проверяем статус-код
    assert resp.status_code == 404, f"Ожидали 404, получили {resp.status_code}"
