# PROBLEM 1

# 1. Share 2 questions you would ask to help understand the question:
#    Will there be any new variables that will be needed in the problem?
#    Will the self.is_caught always equal false?

# 2. Write out in plain English what you want to do:
#    Call the constructor and store the specified name and type.

# 3. Translate each sub-problem into pseudocode:
#    declare my pokemon variable
#    call constructor and input the desired name and type

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

class Pokemon:
  def __init__(self, name, types):
      self.name = name
      self.types = types
      self.is_caught = False

my_pokemon = Pokemon("Pikachu", ["Electric"])
print(my_pokemon.name)
print(my_pokemon.types)


# PROBLEM 2

# 1. Share 2 questions you would ask to help understand the question:
#    How do we call the print_pokemon function?
#    Will we be able to keep adding new objects under the class?

# 2. Write out in plain English what you want to do:
#    Create a new object called squirtle in the Pokemon2 class. Print using the print method provided.

# 3. Translate each sub-problem into pseudocode:
#    Squirtle = Pokemon2(...)
#    Call print function from Pokemon2 class.

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

class Pokemon2:
  def __init__(self, name, types):
      self.name = name
      self.types = types
      self.is_caught = False

  def print_pokemon(self):
      print({
          "name": self.name,   # Output: "name": "Squirtle",
          "types": self.types, # Output: "types": ["Water"],
          "is_caught": self.is_caught # Output: "is_caught": False
      })

squirtle = Pokemon2("Squirtle", ["Water"])
squirtle.print_pokemon()

# PROBLEM 3

# 1. Share 2 questions you would ask to help understand the question:
#    Do we need to change anythin in the print function?
#    Is there a way to update the attribute in the init function without manually adjusting the is_caught.

# 2. Write out in plain English what you want to do:
#    Set the self.is_caught to true.

# 3. Translate each sub-problem into pseudocode:
#    self.is_caught = True

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

class Pokemon3:
  def __init__(self, name, types):
      self.name = name
      self.types = types
      self.is_caught = False

  def print_pokemon(self):
      print({
          "name": self.name,   # Output: "name": "Squirtle",
          "types": self.types, # Output: "types": ["Water"],
          "is_caught": self.is_caught # Output: "is_caught": False
      })

squirtle = Pokemon3("Squirtle", ["Water"])
squirtle.is_caught = True
squirtle.print_pokemon()

# PROBLEM 4

# 1. Share 2 questions you would ask to help understand the question:
#    Will we need to modify other objects?
#    Do we need to set the is_caught attribute back to false?

# 2. Write out in plain English what you want to do:
#    Create a new method to set the is_caught attribute to True when called.

# 3. Translate each sub-problem into pseudocode:
#    Define catch method.
#    Set self.is_caught = True

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

class Pokemon4:
  def __init__(self, name, types):
      self.name = name
      self.types = types
      self.is_caught = False

  def print_pokemon(self):
      print({
          "name": self.name,   # Output: "name": "Squirtle",
          "types": self.types, # Output: "types": ["Water"],
          "is_caught": self.is_caught # Output: "is_caught": False
      })

  def catch(self):
    self.is_caught = True
    pass

my_pokemon = Pokemon4("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.catch()
my_pokemon.print_pokemon()

# PROBLEM 5

# 1. Share 2 questions you would ask to help understand the question:
#    Will we always assume the choose method will call a already caught pokemon?
#    Do we need to account for if we fail to catch the pokemon?

# 2. Write out in plain English what you want to do:
#    Add new method catch. Check if the pokemon is caught, if so print out the choose statement. If not set catch to true.

# 3. Translate each sub-problem into pseudocode:
#    if caught:
#      [pokemon], I choose you!
#    else:
#      A wild [pokemon] appeared! Try catching it!

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

class Pokemon5:
  def __init__(self, name, types):
      self.name = name
      self.types = types
      self.is_caught = False

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

my_pokemon = Pokemon5("Rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()

print("Question 7:")

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