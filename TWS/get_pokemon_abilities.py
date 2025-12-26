import requests # type: ignore

def fetch_pokemon_abilities(base_url, poke, headers):
    abilities = requests.get(base_url+poke, headers=headers)
    return abilities


base_url ="https://pokeapi.co/api/v2/pokemon/"
pokemon = input("Enter pokemon name: ").lower()
# pokemon = "charizard"


headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

print(f"These are the abilities of {pokemon}")
for ability in fetch_pokemon_abilities(base_url, pokemon, headers).json()["abilities"]:
    print(ability["ability"]["name"])


