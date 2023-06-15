from fastapi.responses import JSONResponse
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv('.env')
apiUrl = os.getenv("API_URL")

def countByLetter(letter: str):
  if not letter.isalpha():
    StatusCode = 404
    content =  {
      "error": "El parámetro 'letter' debe ser una letra.",
      }
  else:
    allPokemonsRequest = requests.get(f"{apiUrl}/pokemon?limit=1281")
    allPokemons = json.loads(allPokemonsRequest.text)
    filteredPokemons = [
      pokemon['name'] for pokemon in allPokemons['results'] if letter.lower() in pokemon['name'].lower()
    ]
    pokemonsQuantity = len(filteredPokemons)
    StatusCode = 200
    content =  {
      "quantity": pokemonsQuantity,
      }
  response = JSONResponse(status_code=StatusCode, content=content)
  return response

def getTypes():
  typesRequest = requests.get(f"{apiUrl}/type")
  types = json.loads(typesRequest.text)
  typesName = [
    pokemon['name'] for pokemon in types['results']
  ]
  StatusCode = 200
  content =  {
    "types": typesName,
    }
  response = JSONResponse(status_code=StatusCode, content=content)
  return response

def getAllByType(pokemonType: str):
  typesRequest = requests.get(f"{apiUrl}/type")
  types = json.loads(typesRequest.text)
  typesName = [
    pokemon['name'] for pokemon in types['results']
  ]
  if pokemonType not in typesName:
    StatusCode = 404
    content =  {
      "error": f"El parámetro '{pokemonType}' no corresponde a un tipo de pokemon",
      }
  else:
    typePkemonsRequest = requests.get(f"{apiUrl}/type/{pokemonType}")
    typePokemons = json.loads(typePkemonsRequest.text)
    pokemons = [
      pokemonObject['pokemon']['name'] for pokemonObject in typePokemons['pokemon']
    ]
    StatusCode = 200
    content =  {
      "pokemons": pokemons,
      }
  response = JSONResponse(status_code=StatusCode, content=content)
  return response
