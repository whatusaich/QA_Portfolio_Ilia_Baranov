import requests

BASE_URL = "https://pokeapi.co/api/v2"

def test_get_pokemon_by_name_valid():
    """
    TC-02: Проверка получения покемона по имени
    Ожидаемый результат: статус 200 и name = "ditto"
    """
    resp = requests.get(f"{BASE_URL}/pokemon/ditto", timeout=15)

    # Проверяем статус-код
    assert resp.status_code == 200, f"Ожидали 200, получили {resp.status_code}"

    # Проверяем тело ответа
    data = resp.json()
    assert data.get("name") == "ditto", (
        f'Ожидали name="ditto", получили {data.get("name")}'
    )

