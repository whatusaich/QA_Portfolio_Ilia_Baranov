import requests

BASE_URL = "https://pokeapi.co/api/v2"

def test_get_pokemon_boundary_id_zero():
    """
    TC-09: Проверка запроса покемона с ID=0
    Ожидаемый результат: статус 404
    """
    resp = requests.get(f"{BASE_URL}/pokemon/0", timeout=15)

    # Проверяем статус-код
    assert resp.status_code == 404, f"Ожидали 404, получили {resp.status_code}"

