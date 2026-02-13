# HTTP calls library
import requests

# response data
# response status_code
#   200 -> OK
#   404 -> NOT FOUND
#   500 -> SERVER ERROR

pokeapi_url = "https://pokeapi.co/api/v2/"

def debug():
    print("Hello World!")

def health():
    print("Server status: UP")
    print("Pokemon Availability:", end='')

def fetchPokemon(pokemon: str):
    pokemon_url = pokeapi_url + "pokemon/" + pokemon
    data = requests.get(pokemon_url)
    print(pokeapi_url + "pokemon/" + pokemon)


    try:
        response = requests.get(pokeapi_url + "pokemon/" + pokemon)
        
        data = response.json()

        poke_name      = data["name"]
        poke_id        = data["id"]
        poke_types     = data["types"]
        poke_abilities = data["abilities"]

        formatted_types = ''

        for type in poke_types:
            formatted_types = formatted_types + "\n" + "           - " + type['type']['name']

        formatted_abilities = ''

        for ability in poke_abilities:
            formatted_abilities = formatted_abilities + "\n" + "           - " + ability['ability']['name']

        message = f"""
        Data of {pokemon}:
        Name: {poke_name};
        Pokedex ID: {poke_id};
        Types: {formatted_types};
        Abilities: {formatted_abilities}.
        """

        return message

    except:
        return f"{pokemon} doesn't exist!"



