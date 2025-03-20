# PROBLEM 1

# 1. Share 2 questions you would ask to help understand the question:
#    Will any pokemon start with an HP of 0?
#    How do we set the pokemon's hp to 0?

# 2. Write out in plain English what you want to do:
#    Add attack method into the Pokemon class. If Pokemon is attacked decrease HP and print out remaining HP. If HP is less than or equal to 0, print that the pokemon fainted.

# 3. Translate each sub-problem into pseudocode:
#    set opponent hp -= damage
#    if the opponent's hp is <= 0:
#      oppenent.hp = 0
#      opponent fainted
#    else:
#      pokemon dealt X damage to opponent 

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

class Pokemon():
  def  __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp 
    self.damage = damage 


  def attack(self, opponent):
    opponent.hp -= self.damage
    
    if opponent.hp <= 0:
      opponent.hp = 0
      print(f"{opponent.name} fainted")
    else:
      print(f"{self.name} dealt {self.damage} damage to {opponent.name}")

pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)

# PROBLEM 2

# 1. Share 2 questions you would ask to help understand the question:
#    How do we reference the next node in the list?
#    What if there are two values in a single node?

# 2. Write out in plain English what you want to do:
#    Create two nodes, and point the nodes to each other. (Not a double linked list)

# 3. Translate each sub-problem into pseudocode:
#    Initialize the two nodes
#    point jigglypuff node to wigglytuff node using the ''.next'.

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

class Node2:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

jigglypuff = Node2("Jigglypuff")
wigglytuff = Node2("Wigglytuff")
jigglypuff.next = wigglytuff

print(jigglypuff.value, "->", jigglypuff.next.value)
print(wigglytuff.value, "->", wigglytuff.next)

# PROBLEM 3

# 1. Share 2 questions you would ask to help understand the question:
#    What if the linked list is already empty?
#    Do we need to create a new node as well before inserting new head node?

# 2. Write out in plain English what you want to do:
#    Set the new node as the head of the list. Update pointers.

# 3. Translate each sub-problem into pseudocode:
#    new_node.next = head
#    return the new_node

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

class Node3:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def add_first(head, new_node):
  new_node.next = head
  return new_node

jigglypuff = Node3("Jigglypuff")
wigglytuff = Node3("Wigglytuff")
jigglypuff.next = wigglytuff

new_node = Node3("Ditto")
node_1 = add_first(jigglypuff, new_node)

if node_1.next:
  print(node_1.next.value, "->", node_1.next.next.value)
  if node_1.next.next:
      print(node_1.value, "->", node_1.next.value)


# PROBLEM 4

# 1. Share 2 questions you would ask to help understand the question:
#    How do we find the tail in the linked list?
#    Do we need to check if the linked list will be empty?

# 2. Write out in plain English what you want to do:
#    Loop through the linked list from the head to the last node. Return value of last node.

# 3. Translate each sub-problem into pseudocode:
#    if the linked list is empty:
#      return None
#    set current to head
#    while there is a next node in the list:
#      current = current.next
#    return the value of last node

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

class Node4:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def get_tail(head):
  if not head:
    return None

  current = head

  while current.next:
    current = current.next

  return current.value
  pass

# linked list: num1->num2->num3
head = Node4(10)

num1 = head
tail = get_tail(num1)
print(tail)

# PROBLEM 5

# 1. Share 2 questions you would ask to help understand the question:
#    What if the replacement is a negative value?
#    Will there be duplicate values?

# 2. Write out in plain English what you want to do:
#    Loop through the linked list, and check each node's value and replace them if the value is the same as original value.

# 3. Translate each sub-problem into pseudocode:
#    set current to head
#    while there is still a value for current:
#      if the current value is equl to the original value:
#        replace current value with replacement
#      move to next node

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

class Node5:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def ll_replace(head, original, replacement):
  current = head

  while current:
    if current.value == original:
      current.value = replacement
      
    current = current.next
  pass

num3 = Node5(5)
num2 = Node5(6, num3)
num1 = Node5(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"

class Card():
  def  __init__(self, suit, rank, next = None):
    self.suit = suit
    self.rank = rank
    self.next = next

def print_hand(starting_card):
  cards = []
  current = starting_card
  while current:
      cards.append((current.suit, current.rank))
      current = current.next
  return cards
  pass

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "King")

card_one.next = card_two
card_two.next = card_three

print(print_hand(card_one.next))