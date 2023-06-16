from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_countPokemonsByLetter():
    response = client.get("/pokemons/search/a")
    assert response.status_code == 200
    assert "quantity" in response.json()
    assert isinstance(response.json()["quantity"], int)

    response = client.get("/pokemons/search/1")
    assert response.status_code == 404
    assert response.json() == {"error": "El parámetro 'letter' debe ser una letra."}

def test_getPokemonLocations():
    response = client.get("/pokemons/bulbasaur/locations")
    assert response.status_code == 200
    assert "quantity" in response.json()
    assert isinstance(response.json()["quantity"], int)
    assert "locations" in response.json()
    assert isinstance(response.json()["locations"], list)
    assert all(isinstance(location, str) for location in response.json()["locations"])

    response = client.get("/pokemons/unknown/locations")
    assert response.status_code == 404
    assert response.json() == {"error": "No existe un pokemon con dicho nombre"}

def test_getPokemonsTypes():
    response = client.get("/pokemons/types")
    assert response.status_code == 200
    assert "types" in response.json()
    assert isinstance(response.json()["types"], list)
    assert all(isinstance(location, str) for location in response.json()["types"])

def test_getPokemonsByType():
    response = client.get("/pokemons/types/fire")
    assert response.status_code == 200
    assert "pokemons" in response.json()
    assert isinstance(response.json()["pokemons"], list)
    assert all(isinstance(location, str) for location in response.json()["pokemons"])

    response = client.get("/pokemons/types/football")
    assert response.status_code == 404
    assert response.json() == {"error": "El parámetro 'football' no corresponde a un tipo de pokemon"}