import json

def load_pokedex(name):
    filename = '{}.txt'.format(name)
    with open(filename) as json_file:
        pokedex = json.load(json_file)
        return pokedex