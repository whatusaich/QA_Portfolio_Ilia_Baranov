import requests

BASE_URL = "https://pokeapi.co/api/v2"

def test_get_invalid_pokemon_name():
    """
    TC-05: Проверка запроса несуществующего покемона
    Ожидаемый результат: статус 404
    """
    resp = requests.get(f"{BASE_URL}/pokemon/unknown", timeout=15)

    # Проверяем статус-код
    assert resp.status_code == 404, f"Ожидали 404, получили {resp.status_code}"
