from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import controllers.pokemons as pokemonsController
import controllers.locations as locationsController

app = FastAPI()

# # Configurar los orígenes permitidos en CORS
origins = [
    "http://localhost:3000",
]

# # Agregar middleware de CORS a la aplicación
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)


@app.get("/pokemons/search/{letter}")
def countPokemonsByLetter(letter: str):
  pokemonsQuantity = pokemonsController.countByLetter(letter)
  return pokemonsQuantity

@app.get("/pokemons/{pokemonName}/locations")
def getPokemonLocations(pokemonName: str):
  pokemonLocations = locationsController.getByPokemon(pokemonName)
  return pokemonLocations

@app.get("/pokemons/types")
def getPokemonsTypes():
  pokemons = pokemonsController.getTypes()
  return pokemons

@app.get("/pokemons/types/{type}")
def getPokemonsByType(type: str):
  pokemons = pokemonsController.getAllByType(type)
  return pokemons