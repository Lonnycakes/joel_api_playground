import requests
import json
from pprint import pprint
from api_utils import poke_url, create_pokedex, get_location, get_type
from db_utils import save_pokedex, load_pokedex, get_pokemon_name_db, get_pokemon_number_db, get_location_db, get_type_db

def pokedex_interface():
    pass



'''
What functionality do I want for the Pokedex, and how do I want it to work?

Think about creating an interface that is friendly and understandable.

Tasks as of 8/24/2019:
1. Get the types into the db and create a new pokedex file that includes the types. (DONE: 8/30)
2. Write a function for getting the types from the db. (DONE)
3. Begin writing functionality for the interface.
'''