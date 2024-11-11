# PROBLEM 1

# 1. Share 2 questions you would ask to help understand the question:
#    Will we need to account for different inputs?
#    How do we set the root of a binary tree?

# 2. Write out in plain English what you want to do:
#    Declare root and add the nodes using the TreeNode class.

# 3. Translate each sub-problem into pseudocode:
#    root = TreeNode(10)
#    root.left
#    root.right

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

class TreeNode1:
  def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def printTree(root):
  if root is None:
    return

  print(root.val)
  printTree(root.left)
  printTree(root.right)
    
root = TreeNode1(10)
root.left = TreeNode1(4)
root.right = TreeNode1(6)

printTree(root)

# PROBLEM 2

# 1. Share 2 questions you would ask to help understand the question:
#    What if the inputs are empty?
#    Are there any time/space constraints?

# 2. Write out in plain English what you want to do:
#    Add the two children nodes and check if the sum adds up to the root.

# 3. Translate each sub-problem into pseudocode:
#    Check if the the root will be empty
#    Return the sum of the left and right value and check if that sum is equal to the root.

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

class TreeNode2:
  def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def check_tree2(root):
  if root is None:
    return False

  return root.val == root.left.val + root.right.val
pass

root = TreeNode2(10)
root.left = TreeNode2(4)
root.right = TreeNode2(6)

print(check_tree2(root))

# PROBLEM 3

# 1. Share 2 questions you would ask to help understand the question:
#    Would we have cases where the tree is empty?
#    What hapens if all or some of the inputs are negative?

# 2. Write out in plain English what you want to do:
#    Check if the root is empty, if so return False. If not then add sum of children and compare the sum to the target.

# 3. Translate each sub-problem into pseudocode:
#    Check if root is empty: return false
#    Set the left and right value to 0
#    Grab the values from the left and right node
#    Add the two nodes and compare to the root

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

class TreeNode3:
  def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def check_tree3(root):
  if root is None:
    return False

  left_val = 0
  right_val = 0

  if root.left:
    left_val = root.left.val
  if root.right:
    right_val = root.right.val

  res = left_val + right_val

  return root.val == res
pass

root = TreeNode3(5)
root.left = TreeNode3(3)
root.right = TreeNode3(2)

print(check_tree3(root))


# PROBLEM 4

# 1. Share 2 questions you would ask to help understand the question:
#    Do we return False or None for the output if the tree is empty?
#    What if the tree is an invalid binary tree?

# 2. Write out in plain English what you want to do:
#    Check if the root or leftmost child is present, if so, recurssively follow the leftmost child until we reach the end of the list.

# 3. Translate each sub-problem into pseudocode:
#    Check if root or leftmost child is empty: return None or return value of root
#    Recursively call the left_most(root) 

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

class TreeNode4:
  def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def left_most4(root):
  if root is None:
    return None

  if root.left is None:
    return root.val

  return left_most4(root.left)
    
pass

root = TreeNode4(1)
root.left = TreeNode4(2)
root.right = TreeNode4(5)
root.left = TreeNode4(4)
root.right = TreeNode4(3)

print(left_most4(root))

# PROBLEM 5

# 1. Share 2 questions you would ask to help understand the question:
#    Would we use a for loop or a while loop for an iterative solution?
#    Will we have to account for an invalid tree?

# 2. Write out in plain English what you want to do:
#    Find the leftmost child using an iterative approach.

# 3. Translate each sub-problem into pseudocode:
#    Check if root is None: return None
#    Using a while loop, set the condition to continue the loop only if there is a left node to traverse to
#    return the left most child's value

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

class TreeNode5:
  def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def left_most5(root):
  if root is None:
    return None

  current = root
  while current.left is not None:
    current = current.left

  return current.val
  
pass

root = TreeNode5(1)
root.left = TreeNode5(2)
root.right = TreeNode5(5)
root.left = TreeNode5(4)
root.right = TreeNode5(4)

print(left_most5(root))