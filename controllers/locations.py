from fastapi.responses import JSONResponse
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv('.env')
apiUrl = os.getenv("API_URL")

def getByPokemon(pokemonName: str):
  pokemonRequest = requests.get(f"{apiUrl}/pokemon/{pokemonName}")
  if pokemonRequest.status_code != 200:
    StatusCode = 404
    content =  {
      "error": "No existe un pokemon con dicho nombre",
      }
  else:
    locationRequest = requests.get(f"{apiUrl}/pokemon/{pokemonName}/encounters")
    locations = json.loads(locationRequest.text)
    locationsName = [location['location_area']['name'] for location in locations]
    locationsQuantity = len(locationsName)
    StatusCode = 200
    content =  {
        "locations": locationsName,
        "quantity": locationsQuantity,
        }
  response = JSONResponse(status_code=StatusCode, content=content)
  return response