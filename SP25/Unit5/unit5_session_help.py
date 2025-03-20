class Pokemon:
    def __init__(self, name, types, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution

    def print_pokemon(self):
      print({
          "name": self.name,   # Output: "name": "Squirtle",
          "types": self.types, # Output: "types": ["Water"],
          "is_caught": self.is_caught # Output: "is_caught": False
      })

    def catch(self):
        self.is_caught = True
    pass

    def choose(self):
        if self.is_caught:
            print(f"{self.name} I choose you!")
        else:
            print(f"A wild {self.name} appeared! Try catching it!")
    pass

def evolve(starter_pokemon):
    # Create a list to store the evolutionary line (starting with the given Pokémon)
    evolution = [starter_pokemon]

    # Create a variable to keep track of the current Pokémon
    current_pokemon = starter_pokemon

    # Loop while the current Pokémon has an evolution
    while current_pokemon.evolution:
        # Add the evolved form to the list
        evolution.append(current_pokemon.evolution)
            
        # Move to the next evolved form
        current_pokemon = current_pokemon.evolution

    # Return the full evolutionary line as a list
    return evolution


def get_by_type(my_pokemon, pokemon_type):
    have_type = []

    for pokemon in my_pokemon:
        if pokemon_type in pokemon.types:
            have_type.append(pokemon)

    return have_type

# initializing pokemons
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")

for pokemon in normal_pokemon:
    print(pokemon.name, "-", pokemon.types)

# Creating Pokémon with proper types and evolutions
charizard = Pokemon("Charizard", ["Fire", "Flying"])  # Final evolution (No evolution)
charmeleon = Pokemon("Charmeleon", ["Fire"], charizard)  # Evolves into Charizard
charmander = Pokemon("Charmander", ["Fire"], charmeleon)  # Evolves into Charmeleon

# Running the evolution function
evolution = evolve(charmander)
for pokemon in evolution:
    print(pokemon.name)

