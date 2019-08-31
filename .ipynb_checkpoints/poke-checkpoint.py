import requests
import json
from pprint import pprint
from api_utils import poke_url, create_pokedex, get_location, get_type
from db_utils import save_pokedex, load_pokedex, get_pokemon_name_db, get_pokemon_number_db, get_location_db, get_type_db

# pokedex = load_pokedex('pokedex_file')

# print(pokedex[0])

# pokedex = create_pokedex(poke_url)

# save_pokedex(pokedex, 'pokedex_file')

bulbasaur = get_type(1)
# pprint(bulbasaur['types'])
print(bulbasaur)

charmander = get_type(4)
# pprint(charmander['types'])
print(charmander)

mewtwo = get_pokemon_name('pokedex_file', 150)
print(mewtwo)

mew = get_pokemon_number('pokedex_file', 'mew')
print(mew)

butterfree = get_location_db('pokedex_file', 'butterfree')
print(butterfree)

hitmonlee = get_type_db('pokedex_file', 'hitmonlee')
print(hitmonlee)