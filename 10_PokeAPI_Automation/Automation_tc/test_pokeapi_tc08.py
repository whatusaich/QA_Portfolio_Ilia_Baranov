import requests

BASE_URL = "https://pokeapi.co/api/v2"

def test_get_pokemon_response_structure():
    """
    TC-08: Проверка структуры ответа при запросе покемона по ID=1
    Ожидаемый результат: статус 200 и наличие ключей id, name, abilities, types
    """
    resp = requests.get(f"{BASE_URL}/pokemon/1", timeout=15)

    # Проверяем статус-код
    assert resp.status_code == 200, f"Ожидали 200, получили {resp.status_code}"

    # Проверяем наличие ключей
    data = resp.json()
    for key in ["id", "name", "abilities", "types"]:
        assert key in data, f"В ответе нет ключа '{key}'"

