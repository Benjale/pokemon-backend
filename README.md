# Pokemon Backend Project

## Install Dependecies
    $ pip install -r requirements.txt

## Running the App
    $ uvicorn main:app --reload 

## Running the Tests
    $ pytest

## Litsen Port 
 http://127.0.0.1:8000

## Description
- This application obtains information from the following [API](https://pokeapi.co/api/v2)
- The application of the [pokemon-frontend](https://github.com/Benjale/pokemon-frontend) repository corresponds to a frontend that consumes this api. Then you can test the functionality of the endpoints from that Frontend or by consuming the endpoints directly from the web, postman or another tool
- You must create a file. env containing API_URL= 'https://pokeapi.co/api/v2'
- This application was created with Fastapi
  
## Endpoints
#### 1 Count Pokemons by Letter(s)

    GET /pokemons/search/{letter}

Count the number of pokemons that contain a letter, some letters or a word in their name. The letter(s) of the pokemon must be delivered in {letter}

#### 2 Count Locations by pokemon

    GET /pokemons/{pokemonName}/locations

Count the number of places a pokemon could be found. The name of the pokemon must be delivered in {pokemonName}

#### 3 Get all pokemon types

    GET /pokemons/types

Returns all types of pokemon that exist

#### 4

    GET /pokemons/types/{type}

Returns all pokemons of a specific type. The name of the type must be delivered in {type}