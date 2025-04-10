# PROBLEM 1 [Version 1]

# PROBLEM 1 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#    What if there are two or more values in the tree?
#    What if there are no values in the tree?

# 2. Write out in plain English what you want to do:
#    Utilize recurssion to verify if the nodes are same as root node.

# 3. Translate each sub-problem into pseudocode:
#    Check if the root is empty: return True
#    Check if node value is not equal to root: return False
#    recursively call the helper function to check if the left and right nodes
#    In the main function, check if root is empty: return True
#    return the helper function

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(h)

class TreeNode1():
   def __init__(self, value, left=None, right=None):
       self.val = value

       self.left = left
       self.right = right

def is_univalued_helper(node, value):
  if not node:
    return True
  if node.val != value:
    return False

  return is_univalued_helper(node.left, value) and is_univalued_helper(node.right, value)

def is_univalued(root):
  if not root:
    return True

  return is_univalued_helper(root, root.val)
pass

root = TreeNode1(1)
root.left = TreeNode1(1)
root.right = TreeNode1(1)
root.left.left = TreeNode1(1)
root.left.right = TreeNode1(2)


print(is_univalued(root))

# PROBLEM 2 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#    What if the tree is empty? What do we return?
#    Is there a limit to the height of a tree?

# 2. Write out in plain English what you want to do:
#    Use recurssion to find the height of the tree. 

# 3. Translate each sub-problem into pseudocode:
#    Check if the root is empty: return 0
#    Calculate height of left and right side of the tree
#    Take the larger height and return that value

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(h)

class TreeNode2():
   def __init__(self, value, left=None, right=None):
       self.val = value
       self.left = left
       self.right = right

def height(root):
  if root is None:
    return 0

  left_h = height(root.left)
  right_h = height(root.right)

  return max(left_h, right_h) + 1
pass

root = TreeNode2(4)
root.left = TreeNode2(2)
root.right = TreeNode2(5)
root.left.left = TreeNode2(1)
root.left.right = TreeNode2(3)

print(height(root))

# PROBLEM 3 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#    What if a certain key exists already?
#    What if the tree is empty?

# 2. Write out in plain English what you want to do:
#    Traverse the tree and insert the node into the specified position (key).

# 3. Translate each sub-problem into pseudocode:
#    Check if tree is empty: insert new node as root
#    If key is greater than current node, recurse left
#      If key is less, recurse right
#    If the two keys matches replace current node value

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(h)

class TreeNode3:
  def __init__(self, key, value, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def insert(root, key, value):
  if root is None:
      return TreeNode3(key, value)

  if key < root.key:  
      root.left = insert(root.left, key, value)
  elif key > root.key:  
      root.right = insert(root.right, key, value)
  else:
      root.val = value 

  return root

# Test cases
print("Test case 1: Inserting a new node into an empty tree")
root = None
root = insert(root, 5, "A")
print("Root value:", root.val) 

print("\nTest case 2: Inserting a node to the left subtree")
root = insert(root, 3, "B")
print("Root value:", root.val)  
print("Left child value:", root.left.val)  

print("\nTest case 3: Inserting a node to the right subtree")
root = insert(root, 8, "C")
print("Root value:", root.val)  
print("Right child value:", root.right.val)  


# PROBLEM 4 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#    What if the tree is empty?
#    Will we be given an invalid BST tree?

# 2. Write out in plain English what you want to do:
#    Remove the specified node by using inorder successor if there are two children.

# 3. Translate each sub-problem into pseudocode:
#    Check if node is empty
#    If only one child: use recurssion to remove the node
#    If two child:  replace node with appropriate node
#    Utilize a helper function to find the minimum within a subtree

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(h)

class TreeNode4:
  def __init__(self, key, value, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def find_min(node):
  # Helper function to find the minimum node in the right subtree
  current = node
  while current.left:
      current = current.left
  return current

def remove_bst(root, key):
  # Locate the node to be removed
  if root is None:
      return None

  if key < root.key:
      root.left = remove_bst(root.left, key)
  elif key > root.key:
      root.right = remove_bst(root.right, key)
  else:
      # If the node is a leaf node:
      if root.left is None and root.right is None:
          # Remove the node by redirecting the appropriate child reference of its parent to None
          return None

      # If the node has one parent:
      if root.left is None:
          # Replace the node with its child, updating its parent's nodes child reference appropriately
          return root.right
      elif root.right is None:
          # Replace the node with its child, updating its parent's nodes child reference appropriately
          return root.left

      # If the node has two children:
      # Find the node's inorder successor (smallest node in right subtree)
      min_node = find_min(root.right)

      # Swap the value of the node and its inorder successor
      root.key, root.val = min_node.key, min_node.val

      # Recursively remove the successor (which now has the current node's value)
      root.right = remove_bst(root.right, min_node.key)

  # Return the root of the updated tree
  return root


# Test Cases
def inorder_traversal(root):
  if root:
    inorder_traversal(root.left)
    print(root.key, end=" ")
    inorder_traversal(root.right)
    
# Test Case 1: Removing a leaf node
root = TreeNode4(5, "A", TreeNode4(3, "B"), TreeNode4(8, "C"))
root.left.left = TreeNode4(1, "D")
root.left.right = TreeNode4(4, "E")
root.right.right = TreeNode4(10, "F")
print("Original Tree (Inorder):")
inorder_traversal(root)
print("\n")
root = remove_bst(root, 1)
print("After Removing 1 (Inorder):")
inorder_traversal(root)
print("\n")

# Test Case 2: Removing a node with one child
root = remove_bst(root, 4)
print("After Removing 4 (Inorder):")
inorder_traversal(root)
print("\n")

# Test Case 3: Removing a node with two children
root = remove_bst(root, 5)
print("After Removing 5 (Inorder):")
inorder_traversal(root)
print("\n")

# Test Case 4: Removing from an empty tree
root = None
root = remove_bst(root, 5)
print("Removing from an empty tree:")
inorder_traversal(root)
print("\n")

# PROBLEM 5 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#    What does the current mean in the inoerder_successor function?
#    What if the tree is empty?

# 2. Write out in plain English what you want to do:
#    Create a helper function that traverses to the leftmost child of a subtree. Find the inorder successor, and return it.

# 3. Translate each sub-problem into pseudocode:
#    Have helper functino find leftmost child of a subtree.
#    If the tree is populated, use the find_min function to find the min in a subtree
#    While tree is populated, find inorder sucessor

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(h)

class TreeNode5():
  def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def find_min5(node):
  while node.left:
      node = node.left
  return node

def inorder_successor(root, current):
  if root.right:
    return find_min5(root.right)

  successor = None
  while root:
      if current.val < root.val:
          successor = root
          root = root.left
      elif current.val > root.val:
          root = root.right
      else:
          break
  return successor
  pass

# Helper function to build the test cases
def build_tree():
    # Tree for Test Case 1
    root1 = TreeNode5(20, 20, TreeNode5(10, 10), TreeNode5(30, 30, TreeNode5(25, 25)))

    # Tree for Test Case 2
    root3 = TreeNode5(12, 12, TreeNode5(5, 5), TreeNode5(20, 20))

    # Tree for Test Case 3
    root4 = TreeNode5(25, 25, TreeNode5(15, 15), TreeNode5(30, 30))


    return [(root1, root1),  (root3, root3.right),
            (root4, root4), ]

# Run test cases
test_cases = build_tree()
expected_outputs = [25, 20, 30]

for i, (root, current) in enumerate(test_cases):
    result = inorder_successor(root, current)
    result_key = result.key if result else None
    print(f"Test Case {i+1}: Expected {expected_outputs[i]}, Got {result_key}")





