# PROBLEM 1

# 1. Share 2 questions you would ask to help understand the question:
#    What if only one node in list?
#    What if list is empty?

# 2. Write out in plain English what you want to do:
#    Start at beginning and loop through list checking if the tail points back to the head.

# 3. Translate each sub-problem into pseudocode:
#    Check if list is empty
#    Loop through list and return  true if tail node points to the head node
#    Return false otherwise

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

def is_circular(head):
  if not head:
      return False

  current = head
  while current.next:
      current = current.next
      if current.next == head:
          return True 

  return False

# PROBLEM 2

# 1. Share 2 questions you would ask to help understand the question:
#    What if list is empty?
#    What if list doesn't cycle?

# 2. Write out in plain English what you want to do:
#    Utilize Floyd's cycle detecting. Locate last node in cycle

# 3. Translate each sub-problem into pseudocode:
#    Check if list is empty
#    Create two pointers
#    Use Floyd's cycle detection
#    If no cycle return none
#    Find start of cycle
#    Then find the last node in the cycle
#    return last node

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

def find_last_node_in_cycle(head):
  if not head or not head.next:
      return None

  slow = fast = head
  has_cycle = False

  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
          has_cycle = True
          break
        
  if not has_cycle:
      return None
    
  slow = head
  
  while slow != fast:
      slow = slow.next
      fast = fast.next

  cycle_start = slow
  last_node = cycle_start
  
  while last_node.next != cycle_start:
      last_node = last_node.next

  return last_node

# PROBLEM 3

# 1. Share 2 questions you would ask to help understand the question:
#    What if list is empty?
#    What if two values are equal?

# 2. Write out in plain English what you want to do:
#    Create two lists for lesser than and greater than values.

# 3. Translate each sub-problem into pseudocode:
#    Create two linked lists
#    create pointers
#    Loop through original list separating the values
#    Stop the greater than list
#    attach less than list
#    return list

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

class Node3:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def partition(head, val):
  less_head = Node3(0)
  greater_head = Node3(0)

  less = less_head
  greater = greater_head

  current = head
  
  while current:
      if current.val < val:
          less.next = current
          less = less.next
      else:
          greater.next = current
          greater = greater.next

      current = current.next

  greater.next = None

  less.next = greater_head.next

  return less_head.next

# PROBLEM 4

# 1. Share 2 questions you would ask to help understand the question:
#    What if list is empty?
#    What does "the most signiicant bit is at the head of linked list" mean?

# 2. Write out in plain English what you want to do:
#    Loop through list while building the binary number.

# 3. Translate each sub-problem into pseudocode:
#    set a variable
#    traverse the list creating the binary number
#    return variable

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def binary_to_int(head):
  num = 0
  current = head
  while current:
      num = num * 2 + current.value
      current = current.next
  return num

num1 = 1
num2 = 0
num3 = 1

int_num = binary_to_int(num1)
# 101 in binary 

print(int_num)

# PROBLEM 5

# 1. Share 2 questions you would ask to help understand the question:
#    What if linked list is empty?
#    What if one linked list is larger than the other?

# 2. Write out in plain English what you want to do:
#    Loop through both linked list add up digits along the way. Form new linked list

# 3. Translate each sub-problem into pseudocode:
#    Create temp node
#    set current to temp node
#    set a variable to keep track
#    loop through both list, add values that have a carry
#    store the carry values inside the result list
#    Handle any remaining nodes that are part of a longer list

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(max(n,m)) - dependent on longest linked list
# Space Complexity: O(max(n,m)) -  dependent on length of longest linked list

class Node5:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def add_two_numbers(head_a, head_b):
  temp_head = Node5(4)
  current = temp_head
  carry = 0

  a_curr = head_a
  b_curr = head_b
  
  while a_curr or b_curr or carry:
      val_a = a_curr.value if a_curr else 0
      val_b = b_curr.value if b_curr else 0

      sum_val = val_a + val_b + carry
      carry = sum_val // 10
      sum_val = sum_val % 10

      current.next = Node5(sum_val)
      current = current.next
    
      if a_curr:
          a_curr = a_curr.next
      if b_curr:
          b_curr = b_curr.next

  return temp_head.next