import json
import requests
from api_utils import get_type
from db_utils import save_pokedex, load_pokedex

def add_type(file_name):
    pokedex = load_pokedex(file_name)
    new_pokedex = pokedex.copy()
    for index, pokemon in enumerate(pokedex):
        ID = pokemon['number']
        pokemon_type = get_type(ID)
        new_pokedex[index].setdefault('types', pokemon_type)
    save_pokedex(new_pokedex, file_name)
    print('Pokedex updated with types!')
    
add_type("pokedex_file")