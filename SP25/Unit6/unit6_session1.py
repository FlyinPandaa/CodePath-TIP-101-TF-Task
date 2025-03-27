# PROBLEM 1

# 1. Share 2 questions you would ask to help understand the question:
#    Can the list be empty?
#    Do we need a entire new function for this question?

# 2. Write out in plain English what you want to do:
#    Access the node class and create the linked list.

# 3. Translate each sub-problem into pseudocode:
#    class(values(class2(values(class3(values)))

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

class Node1:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

Node1(4, Node1(3, Node1(2)))

# PROBLEM 2

# 1. Share 2 questions you would ask to help understand the question:
#    What happens if the list is empty?
#    Would it be possible to solve the problem in O(1) time?

# 2. Write out in plain English what you want to do:
#    Loop through linked list, compare each value to the target, increment counter if they  match.

# 3. Translate each sub-problem into pseudocode:
#    count = 0
#    loop through linked list:
#    if match target then increment count
#    return count

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

class Node2:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def count_element(val, lst):
  count = 0
  
  for current in lst:
    if current == val:
      count += 1
      
  return count

print(count_element(3, [1, 2, 3, 4, 3, 5]))

# PROBLEM 3

# 1. Share 2 questions you would ask to help understand the question:
#    Can the input linked list be empty?
#    Should we print out the new linked list?

# 2. Write out in plain English what you want to do:
#    Print statements to track state of linked list. Go through list and remove the last node.

# 3. Translate each sub-problem into pseudocode:
#    Check if linked list is empty
#    Check if the linked list has only one item
#    Loop through linked  list and  remove the last node
#    print out the output

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

class Node3:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def remove_tail(head):
    if head is None:
        print("List is empty. No tail to remove.")
        return None
    if head.next is None:
        print("Only one node in the list. Removing the node.")
        return None

    current = head
    
    while current.next.next:
        print(f"Current Node: {current.value} -> Next Node: {current.next.value}")
        current = current.next
        
    print(f"Removing tail node with value: {current.next.value}")
    current.next = None
  
    current = head
    while current:
        print(current.value, end=" ")
        current = current.next
    print()
  
    return head

head = Node3(1, Node3(2, Node3(3, Node3(4))))

print(remove_tail(head))

# PROBLEM 4

# 1. Share 2 questions you would ask to help understand the question:
#    What if linked list is empty?
#    What if there is an even number of nodes?

# 2. Write out in plain English what you want to do:
#    With two pointers, have one move at half of the speed as the other pointer. Find middle.

# 3. Translate each sub-problem into pseudocode:
#    create slow and fast pointer
#    loop through the linked list with the pointers, one moving faster.
#    return the slow pointer

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

class Node4:
  def __init__(self, value=None, next=None):
      self.value = value
      self.next = next

def find_middle_element(head):
  slow = fast = head
  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
  return slow.value
  
head = Node4(1, Node4(2, Node4(3, Node4(4))))

print(find_middle_element(head))

# PROBLEM 5

# 1. Share 2 questions you would ask to help understand the question:
#    What if multiple data types?
#    What if the linked list is empty?

# 2. Write out in plain English what you want to do:
#    Use two pointer to find the middle of list, and then reverse the second half.

# 3. Translate each sub-problem into pseudocode:
#    Check if there is only one item in list or no item
#    loop through list with pointer
#    reverse list

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

class Node5:
  def __init__(self, value=None, next=None):
      self.value = value
      self.next = next

def is_palindrome(head):
  if head is None or head.next is None:
      return True

  slow = fast = head
  
  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

  prev = None
  
  while slow:
      next_node = slow.next
      slow.next = prev
      prev = slow
      slow = next_node

  left, right = head, prev
  
  while right:  
      if left.value != right.value:
          return False
      left = left.next
      right = right.next

  return True