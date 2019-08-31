import json

def save_pokedex(pokedex, name):
    pokedex_file = '{}.txt'.format(name)
    with open(pokedex_file, 'w') as outfile:
        json.dump(pokedex, outfile, indent=4)

def load_pokedex(pokedex_file):
    filename = '{}.txt'.format(pokedex_file)
    with open(filename) as json_file:
        pokedex = json.load(json_file)
        return pokedex
    
def get_pokemon_name_db(file_name, number):
    pokedex = load_pokedex(file_name)
    for pokemon in pokedex:
        if number == pokemon["number"]:
            return pokemon["name"]

def get_pokemon_number_db(file_name, name):
    pokedex = load_pokedex(file_name)
    for pokemon in pokedex:
        if name == pokemon['name']:
            return pokemon['number']

def get_location_db(file_name, ID):
    pokedex = load_pokedex(file_name)
    for pokemon in pokedex:
        if ID == pokemon['name'] or ID == pokemon['number']:
            return pokemon['locations']

def get_type_db(file_name, ID):
    pokedex = load_pokedex(file_name)
    for pokemon in pokedex:
        if ID == pokemon['name'] or ID == pokemon['number']:
            return pokemon['types']
    
'''
get_pokemon - gets all the Pokemon data in the dictionary

What functionality do I want for the Pokedex, and how do I want it to work?

THink about creating an interface that is friendly and understandable.

Tasks as of 8/24/2019:
1. Get the types into the db and create a new pokedex file that includes the types. (DONE: 8/30)
2. Write a function for getting the types from the db. (DONE)
3. Begin writing functionality for the interface.

'''