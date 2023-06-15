from fastapi import FastAPI
import controllers.pokemons as pokemonsController
import controllers.locations as locationsController

app = FastAPI()

@app.get("/pokemons/search/{letter}")
async def countPokemonsByLetter(letter: str):
  pokemonsQuantity = pokemonsController.countByLetter(letter)
  return pokemonsQuantity

@app.get("/pokemons/{pokemonName}/locations")
async def getPokemonLocations(pokemonName: str):
  pokemonLocations = locationsController.getByPokemon(pokemonName)
  return pokemonLocations

@app.get("/pokemons/types")
async def getPokemonsTypes():
  pokemons = pokemonsController.getTypes()
  return pokemons

@app.get("/pokemons/types/{type}")
async def getPokemonsByType(type: str):
  pokemons = pokemonsController.getAllByType(type)
  return pokemons