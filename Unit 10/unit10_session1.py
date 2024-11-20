# PROBLEM 1

# 1. Share 2 questions you would ask to help understand the question:
#    What should we return if the string is empty?
#    Will we only be given parantheses/brackets or will there be integers mixed in?

# 2. Write out in plain English what you want to do:
#    Initialize a stack and keep track of all unclosed parantheses/brackets. When a closing parantheses/brackets is encountered. Pop the unclosed parantheses/brackets from the stack.

# 3. Translate each sub-problem into pseudocode:
#    Initialize stack and a dictionary of brackets
#    Iterate through the string
#      When encountering a bracket, check if the bracket is the one we are looking for
#      If not, return false
#    Otherwise append the bracket to the stack

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n) - Looping through the entire string.
# Space Complexity: O(n) - Using a stack

def is_valid(s):
  stack = []
  bracket_map = {')': '(', '}': '{', ']': '['}

  for char in s:
      if char in bracket_map:
          top_element = stack.pop() if stack else '#'
          if bracket_map[char] != top_element:
              return False
      else:
          stack.append(char)

  return not stack

# Another possible solution

# def is_valid(s):
#     stack = []  # Initialize the stack to keep track of opening brackets
#     matching = {')': '(', '}': '{', ']': '['}  # Map of closing to opening brackets

#     for char in s:
#         if char in matching:  # If the character is a closing bracket
#             # Pop the top of the stack if not empty, otherwise use a placeholder '#'
#             top_element = stack.pop() if stack else '#'
#             # Check if the top element matches the current closing bracket
#             if matching[char] != top_element:
#                 return False
#         else:
#             stack.append(char)  # Push opening brackets onto the stack

#     return not stack  # The stack should be empty if all brackets are matched

print(is_valid("()[]{}"))

print(is_valid("([{}])"))

print(is_valid("({[)]}"))

# PROBLEM 2

# 1. Share 2 questions you would ask to help understand the question:
#    What if the prices list is empty?
#    Will we encounter negative numbers?

# 2. Write out in plain English what you want to do:
#    Loop through the list while keeping track of the min price to get the max profit for each element in the list.

# 3. Translate each sub-problem into pseudocode:
#    Initialize variables
#    Loop through the prices in the list
#      Find min price
#      Calculate the profit
#      Update the profit if a higher profit is calculated
#    Return the proft

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n) - Looping through a list of integers
# Space Complexity: O(1) - Only using a constant amount of space

def max_profit(prices):
  min_price = float('inf')
  max_profit = 0

  for price in prices:
      min_price = min(min_price, price)
      current_profit = price - min_price
      max_profit = max(max_profit, current_profit)

  return max_profit

print(max_profit([7,1,5,3,6,4]))

print(max_profit([7,6,4,3,1]))

print(max_profit([1,2,3,4,5]))

# PROBLEM 3

# 1. Share 2 questions you would ask to help understand the question:
#    What if both or one of the linked list is empty?
#    How do we return the head of the linked list?

# 2. Write out in plain English what you want to do:
#    Use two pointer technique to traverse the two linked list. Alternately add nodes to the merged list. Append the rest of the nodes into the merged list if there are remaining nodes in one list.

# 3. Translate each sub-problem into pseudocode:
#    Check if either lists are empty
#    Create the merged list
#    Alternate between the two lists and merge nodes
#    when one list is empty, merge the remaining nodes from the other list into the merged list
#    Return the merged list

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n) - Traversing two linked list
# Space Complexity: O(1) - Only using constant amount of space

def shuffle_merge(head_a, head_b):
  if not head_a:
      return head_b
  if not head_b:
      return head_a
    
  merged_head = head_a
  current_a = head_a.next
  current_b = head_b
  current_merged = merged_head
  
  toggle = True
  while current_a and current_b:
      if toggle:
          current_merged.next = current_b
          current_b = current_b.next
      else:
          current_merged.next = current_a
          current_a = current_a.next
      current_merged = current_merged.next
      toggle = not toggle
    
  
  current_merged.next = current_a if current_a else current_b
  
  return merged_head

# No test cases

# PROBLEM 4

# 1. Share 2 questions you would ask to help understand the question:
#    What if the string is empty?
#    What if there is only one element in the string?

# 2. Write out in plain English what you want to do:
#    Utilize hash map to group anagrams.

# 3. Translate each sub-problem into pseudocode:
#    Initialize an empty hash map
#    Loop through each word in the list:
#      Sort character accordinly
#    Create an empty list
#    Append the correct grouping into the empty list and return it

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n) - Has to loop through an input list
# Space Complexity: O(n) - Using additional space with the dictionaries

def group_anagrams(strs):
  anagrams_dict = {}

  for word in strs:
      word_as_list = list(word)
      word_as_list.sort()
      key = tuple(word_as_list)
    
      if anagrams_dict.get(key):
          anagrams_dict[key].append(word)
      else:
          anagrams_dict[key] = [word]

  answer = []

  for key, value in anagrams_dict.items():
    answer.append(value)
    
  return answer

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print(group_anagrams(["", " "]))

print(group_anagrams(["a"]))

# PROBLEM 5

# 1. Share 2 questions you would ask to help understand the question:
#    What if tree is empty?
#    What if there are no leaf nodes?

# 2. Write out in plain English what you want to do:
#    Utilize DFS helper function to traverse tree. If leaf node add value to total sum.

# 3. Translate each sub-problem into pseudocode:
#    Define a DFS function
#    Initialize the DFS with the root node
#    return result

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n) - Need to loop through each node
# Space Complexity: O(n) - Based on height of the tree

class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def sum_numbers(root):
  def dfs(node, current_number):
      if node is None:
          return 0

      current_number = current_number * 10 + node.val
    
      if node.left is None and node.right is None:
          return current_number

      left_sum = dfs(node.left, current_number)
      right_sum = dfs(node.right, current_number)

      return left_sum + right_sum

  return dfs(root, 0)

# Test Case 1:
# Tree:
#     1
#    / \
#   2   3
#  / \
# 4   5
# Expected Output: 124 + 125 + 13 = 262
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(sum_numbers(root))  # Output: 262

# Test Case 2:
# Tree:
#     4
#    / \
#   9   0
#  / \
# 5   1
# Expected Output: 495 + 491 + 40 = 926

root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
print(sum_numbers(root))  # Output: 926

# Test Case 3:
# Tree:
#     1
#    / 
#   2
#  /
# 3
# Expected Output: 123
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
print(sum_numbers(root))  # Output: 123
