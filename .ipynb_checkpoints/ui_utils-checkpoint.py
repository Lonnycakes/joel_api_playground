from db_utils import *

def main_menu():
    pass

def get_pokemon_by_name():
    poke_name = input('Please type the name of the Pokemon.\n').lower()
    pokedex = load_pokedex('pokedex_file')
    for pokemon in pokedex:
        if poke_name in pokemon['name']:
            return pokemon
    
def get_pokemon_by_number():
    try:
        poke_number = int(input('Please type the number of the Pokemon.\n'))
        pokedex = load_pokedex('pokedex_file')
        for pokemon in pokedex:
            if poke_number == pokemon['number']:
                return pokemon
    except:
        print('You must type in a number.')
        pokemon = get_pokemon_by_number()
        return pokemon
        
def get_pokemon_by_type():
    type_list = 'Fire, Water, Grass, Eletric, Psychic, Steel, Normal, Fairy, Dark, Flying, Ghost, Poison, Ice, Ground, Rock, Dragon, Fighting, Bug'.split(', ')
    for i in range(6):
        print('     \t'.join(type_list[i*3:i*3+3]))
    poke_type_1 = input('Please enter a Pokemon type.\n').lower()
    pokedex = load_pokedex('pokedex_file')
    results = []
    for pokemon in pokedex:
        if poke_type_1 in pokemon['types']:
            results.append(pokemon)
    print([pokemon['name'].capitalize() for pokemon in results])
            
#            Try to write a way to sort the results of type 1 to filter by a second type.

# After, try to write a way to search for POkemon by location.
            
            
get_pokemon_by_type()

        
# rando = get_pokemon_by_number()
# print(rando)
    
def display_pokemon(pokemon):
    name = pokemon['name'].capitalize()
    type_string = ' and '.join(pokemon['types'])
    pokemon_number = pokemon['number']
    loc_string = pokemon['locations'][0]
    if loc_string != 'This Pokemon cannot be encountered in the wild.':
        loc_string = 'This Pokemon can found in {} different locations.'.format(len(pokemon['locations']))
    
    output = '''
    {name}!
    It is a {type_string} type Pokemon.
    Its number is {pokemon_number}.
    {loc_string}
    '''.format(
    name = name,
    type_string = type_string,
    pokemon_number = pokemon_number,
    loc_string = loc_string
    )
    
    return output

pokedex = load_pokedex('pokedex_file')
some_pokemon = pokedex[123]
display_pokemon(some_pokemon)
    

'''
Hello, Pokemon Trainer!
What would you like to do today?

- Look up all Pokemon info based on the name or number
    - Show number, number of locations, and types
    - Offer the option to see detailed info on locations
- Find a Pokemon by location, name, number, type
'''