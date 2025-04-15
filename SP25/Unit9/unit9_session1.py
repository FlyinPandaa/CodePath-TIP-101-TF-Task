# PROBLEM 1 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#    Can the tree be empty?
#    Will all tree inputs be equal in height?

# 2. Write out in plain English what you want to do:
#    Utilize a helper function to compare both left and right subtrees.

# 3. Translate each sub-problem into pseudocode:
#    if the tree is empty: return true
#    if only one subtree is none: return false
#    if the values don't match: return false
#    recursively call helper function

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(n)
# Space complexity: O(h)

class TreeNode1:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def is_mirror(left, right):
  if not left and not right:
      return True
  if not left or not right:
      return False
  if left.val != right.val:
      return False
    
  return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

def is_symmetric(root):
  if not root: 
    return True
    
  return is_mirror(root.left, root.right)
pass

# Test case 1: Symmetric tree
root = TreeNode1(1)
root.left = TreeNode1(2)
root.right = TreeNode1(2)
root.left.left = TreeNode1(3)
root.left.right = TreeNode1(4)
root.right.left = TreeNode1(4)
root.right.right = TreeNode1(3)
print(is_symmetric(root))

# Test case 2: Asymmetric tree
root = TreeNode1(1)
root.left = TreeNode1(2)
root.right = TreeNode1(3)
root.left.left = TreeNode1(4)
root.left.right = TreeNode1(5)
print(is_symmetric(root))

# Test case 3: Empty tree
root = None
print(is_symmetric(root))

# PROBLEM 2 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#    Will we ever run into an empty tree?
#    How should we handle a no-leaf node tree?

# 2. Write out in plain English what you want to do:
#    Store the list of nodes (path) while using depth first search to traverse all nodes until encountering a leaf node.

# 3. Translate each sub-problem into pseudocode:
#    Initialize an empty list
#    Create a hlper function that will perform the depth first search
#    Call the helper function in the main function
#    return the populated list

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(n)
# Space complexity: O(h)

class TreeNode2:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def dfs(node, path, paths):
  if not node:
      return

  # Append current node value to path
  if path:
      path += "->" + str(node.val)
  else:
      path = str(node.val)

  # Check if it's a leaf node
  if not node.left and not node.right:
      paths.append(path)
  else:
      # Continue to explore the left and right subtree
      dfs(node.left, path, paths)
      dfs(node.right, path, paths)

def binary_tree_paths(root):
  paths = []
  dfs(root, """""", paths)
  pass

# Test case 1: Simple tree
root = TreeNode2(1)
root.left = TreeNode2(2)
root.right = TreeNode2(3)
print(binary_tree_paths(root))

# Test case 2: Tree with a single leaf node
root = TreeNode2(1)
root.left = TreeNode2(2)
root.left.left = TreeNode2(4)
print(binary_tree_paths(root))

# Test case 3: Empty tree
root = None
print(binary_tree_paths(root))

# PROBLEM 3 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#    Will we always be guranteed a valid binary search tree?
#    Will we have to account for an empty tree?

# 2. Write out in plain English what you want to do:
#    Get a sorted list of node values, then find the minimum value.

# 3. Translate each sub-problem into pseudocode:
#    Initialize empty list
#    Create a helper function that will traverse the tree (inorder)
#    Call the helper function in the main function
#    Initialize the minimum difference variable
#    Loop through list to find the min value
#    Return minimum

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(n)
# Space complexity: O(n)

class TreeNode3:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def inorder_traversal(root, nodes):
  if root is not None:
      inorder_traversal(root.left, nodes)
    
      nodes.append(root.val)
    
      inorder_traversal(root.right, nodes)

def min_diff_in_bst(root):
  nodes = []
  inorder_traversal(root, nodes)

  min_diff = float('inf')

  for i in range (1, len(nodes)):
    min_diff = min(min_diff, nodes[i] - nodes[i - 1])

  return min_diff
pass

# Test Case 1: Simple BST
root = TreeNode3(4)
root.left = TreeNode3(2)
root.right = TreeNode3(6)
root.left.left = TreeNode3(1)
root.left.right = TreeNode3(3)
print(min_diff_in_bst(root))

# Test Case 2: BST with larger differences
root = TreeNode3(10)
root.left = TreeNode3(5)
root.right = TreeNode3(15)
root.left.left = TreeNode3(1)
root.left.right = TreeNode3(8)
print(min_diff_in_bst(root))

# Test Case 3: Empty BST
root = None
print(min_diff_in_bst(root))

# PROBLEM 4 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#    Can the tree be empty? What do we return?
#    What if there is no left-most node?

# 2. Write out in plain English what you want to do:
#    Using in-order traversal, traverse the tree and put nodes into list. Create a new root for the tree starting with the first value in the list.

# 3. Translate each sub-problem into pseudocode:
#    Create empty list
#    Define helper function that will perform the inorder traversal
#    Call the helper function in the main function 
#    Create new root, and have each new node moved to the right child of the current node

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(n)
# Space complexity: O(h)

class TreeNode4:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def inorder_trav(root, nodes):
  if root:
      inorder_trav(root.left, nodes)
    
      nodes.append(root.val)
    
      inorder_trav(root.right, nodes)

def increasing_bst(root):
  nodes = []

  inorder_trav(root, nodes)

  new_root =  TreeNode4(nodes[0])
  current = new_root

  for i in nodes[1:]:
    current.right = TreeNode4(i)
    current = current.right

  return new_root
pass

# Test Case 1: Simple BST
root = TreeNode4(5)
root.left = TreeNode4(3)
root.right = TreeNode4(8)
root.left.left = TreeNode4(1)
root.left.right = TreeNode4(4)
new_root = increasing_bst(root)

# Print
def inorder_print(node):
    if node:
        inorder_print(node.left)
        print(node.val, end=" ")
        inorder_print(node.right)
      
inorder_print(new_root)

# PROBLEM 5 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#    What if the tree is empty?
#    Can we use helper functions?

# 2. Write out in plain English what you want to do:
#    Count total number of nodes in the tree. Check if the subtrees have half of the total number of nodes in the tree.

# 3. Translate each sub-problem into pseudocode:
#    Define helper function to count number of nodes in tree
#    Define helper function that will perform DFS to determine if the subtrees can be split
#    In main function determine if the split can happen. If yes split tree.
#    return true or false depending on whether or not the tree can be split

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(n)
# Space complexity: O(h)

class TreeNode5:
  def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def count_nodes(root):
  if not root:
      return 0
    
  return 1 + count_nodes(root.left) + count_nodes(root.right)

class TreeSplitter:
  def __init__(self):
    self.found = False 
    
  def dfs_split(self, root, total_nodes):
    if not root:
      return 0

    left_count = self.dfs_split(root.left, total_nodes)
    right_count = self.dfs_split(root.right, total_nodes)

    
    if left_count == total_nodes // 2 or right_count == total_nodes // 2:    
      self.found = True
    return 1 + left_count + right_count
    
def can_split(root):
  if not root:
    return False

  total_nodes = count_nodes(root)
  splitter = TreeSplitter()
  splitter.dfs_split(root, total_nodes)
  return splitter.found

# Test Case 1: Splitable tree
root = TreeNode5(1)
root.left = TreeNode5(2)
root.right = TreeNode5(3)
root.left.left = TreeNode5(4)
root.left.right = TreeNode5(5)
print(can_split(root))

# Test Case 2: Non-splitable tree
root = TreeNode5(1)
root.left = TreeNode5(2)
root.right = TreeNode5(3)
root.left.left = TreeNode5(4)
print(can_split(root))

# Test Case 3: Empty tree
root = None
print(can_split(root))  
