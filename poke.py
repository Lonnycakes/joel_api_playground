import requests
import json
from pprint import pprint
from api_utils import poke_url, save_pokedex, create_pokedex, load_pokedex, get_location, get_type

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