import requests

BASE_URL = "https://pokeapi.co/api/v2"

def test_get_pokemon_by_id_valid():
    # TC-01: Проверяем, что покемон с ID=1 — это bulbasaur
    resp = requests.get(f"{BASE_URL}/pokemon/1", timeout=15)
    assert resp.status_code == 200, f"Ожидали 200, получили {resp.status_code}"
    data = resp.json()
    assert data.get("name") == "bulbasaur", f'Ожидали name="bulbasaur", получили {data.get("name")}'


