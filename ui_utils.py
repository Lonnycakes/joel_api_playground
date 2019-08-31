from db_utils import *

def main_menu():
    pass

def display_pokemon(pokemon):
    name = pokemon['name']
    type_string = ' and '.join(pokemon['types'])
    pokemon_number = pokemon['number']
    loc_string = ''
    # if
    
    output = '''
    {name}!
    It is a {type_string} type Pokemon.
    Its number is {pokemon_number}.
    {loc_string}
    '''
    pass
    
def main_menu():
    pass


'''
Hello, Pokemon Trainer!
What would you like to do today?

- Look up all Pokemon info based on the name or number
    - Show number, number of locations, and types
    - Offer the option to see detailed info on locations
- Find a Pokemon by location, name, number, type

NEXT TIME (8/31/2019):
    - Write for the "loc_number" string.
        - Has to say 2 different things:
            The number of locations;
            Or, that it does not appear in the wild.
    - 

'''