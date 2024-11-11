from collections import deque

# PROBLEM 1

# 1. Share 2 questions you would ask to help understand the question:
#    Will we get empty trees?
#    Does the tree need to be a valid BST?

# 2. Write out in plain English what you want to do:
#    Using BFS, traverse th tree. Use a queue to keep track of nodes that have been visited.

# 3. Translate each sub-problem into pseudocode:
#    If tree empty: return empty list
#    Initialize empty queue and list to store explored nodes
#    Set root to the empty queue
#    Iterate through tree and visit each node
#    Return the list

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(n) Will have to visit each node in the tree at least once.
# Space complexity: O(n) Using a queue

class TreeNode1:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if root is None:
        return []

    queue = deque()
    visited = []
    queue.append(root)

    while queue:
        current_node = queue.popleft()

        visited.append(current_node.val)

        if current_node.left is not None:
            queue.append(current_node.left)

        if current_node.right is not None:
            queue.append(current_node.right)

    return visited

# Case 1: Empty Tree
root1 = None
print(f"Case 1: Empty Tree, Expected: [], Actual: {level_order(root1)}")
assert level_order(root1) == []

# Case 2: Single Node
root2 = TreeNode1(1)
print(f"Case 2: Single Node, Expected: [1], Actual: {level_order(root2)}")
assert level_order(root2) == [1]

# Case 3: Simple Tree
root3 = TreeNode1(1, TreeNode1(2), TreeNode1(3))
print(f"Case 3: Simple Tree, Expected: [1, 2, 3], Actual: {level_order(root3)}")
assert level_order(root3) == [1, 2, 3]

# PROBLEM 2

# 1. Share 2 questions you would ask to help understand the question:
#    What if tree is empty?
#    What if there are no leaf nodes?

# 2. Write out in plain English what you want to do:
#    Return depth of the leaf node when encountered using the BFS approach.

# 3. Translate each sub-problem into pseudocode:
#    If tree is empty: return 0
#    Create empty queue and root node as depth of 1
#    While there are nodes:
#      go through each node in the queue and return dept of that node
#    return 0 when reaching end of code without a proper return from while loop

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(n) Will have to visit input and pop each node once.
# Space complexity: O(n) Using a queue

class TreeNode2:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def min_depth(root):
  if not root:
      return 0

  queue = deque()  # The queue stores tuples of (node, depth)
  queue.append((root, 1))

  while queue:
      node, depth = queue.popleft()

      # Check if the current node is a leaf node
      if not node.left and not node.right:
          return depth

      # Add the left child to the queue if it exists
      if node.left:
          queue.append((node.left, depth + 1))

      # Add the right child to the queue if it exists
      if node.right:
          queue.append((node.right, depth + 1))

  return 0  # This line will never be reached if the input tree is valid

# Case 1: Empty Tree
root1 = None
print(f"Case 1: Empty Tree, Expected: 0, Actual: {min_depth(root1)}")
assert min_depth(root1) == 0

# Case 2: Single Node
root2 = TreeNode2(1)
print(f"Case 2: Single Node, Expected: 1, Actual: {min_depth(root2)}")
assert min_depth(root2) == 1

# Case 3: Simple Tree
root3 = TreeNode2(1, TreeNode2(2), TreeNode2(3))
print(f"Case 3: Simple Tree, Expected: 2, Actual: {min_depth(root3)}")
assert min_depth(root3) == 2

# PROBLEM 3

# 1. Share 2 questions you would ask to help understand the question:
#    What if the tree is empty?
#    What if there is only a single node?

# 2. Write out in plain English what you want to do:
#    Traverse the tree using BFS and use a queue to keep track of nodes and their level on the tree. Initialize two sums (one for odd and even each). Return the difference at the end.

# 3. Translate each sub-problem into pseudocode:
#    If empty tree: return 0
#    Create empty queue
#    Initialize sums for even and odd
#    While the queue is not empty: get level of node and pop node out of queue
#      Advance to next level of tree
#    return difference

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(n) Will have to visit each node once.
# Space complexity: O(n) Using a queue

class TreeNode3:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def level_difference(root):
  if not root:
      return 0

  queue = deque([root])
  level = 1

  odd_sum = 0
  even_sum = 0

  while queue:
      level_size = len(queue)

      for _ in range(level_size):
          node = queue.popleft()

          if level % 2 == 1:
              odd_sum += node.val
          else:
              even_sum += node.val

          if node.left:
              queue.append(node.left)
              # Increment level for the left child
              level += 1 
          if node.right:
              queue.append(node.right)
              # Increment level for the right child
              level += 1  

  return odd_sum - even_sum

# Case 1: Empty Tree
root1 = None
print(f"Case 1: Empty Tree, Expected: 0, Actual: {level_difference(root1)}")
assert level_difference(root1) == 0

# Case 2: Single Node
root2 = TreeNode3(1)
print(f"Case 2: Single Node, Expected: 1, Actual: {level_difference(root2)}")
assert level_difference(root2) == 1

# # Case 3: Simple Tree
# root3 = TreeNode3(1, TreeNode3(2), TreeNode3(3))
# print(f"Case 3: Simple Tree, Expected: -1, Actual: {level_difference(root3)}")
# assert level_difference(root3) == -1

# PROBLEM 4

# 1. Share 2 questions you would ask to help understand the question:
#    What if tree is empty?
#    What is a list of lists?

# 2. Write out in plain English what you want to do:
#    Traverse tree by using BFS. Use queue to keep track of nodes in that haven't been visited. Initialize  a list of lists to store nodes.

# 3. Translate each sub-problem into pseudocode:
#    If empty tree: return empty list
#    Create empty queue and list
#    Add root to the queue
#    While there are nodes in the queue: traverse through nodes
#    return result

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(n) Will have to visit each node once.
# Space complexity: O(n) Using a queue

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def level_order(root):
  if not root:
      return []

  res= []
  queue = deque()
  queue.append(root)

  while queue:
      level_size = len(queue)
      level_nodes = []

      for i in range(level_size):
          node = queue.popleft()
          level_nodes.append(node.val)

          if node.left:
              queue.append(node.left)
          if node.right:
              queue.append(node.right)

      res.append(level_nodes)

  return res

# Case 1: Empty Tree
root1 = None
print(f"Case 1: Empty Tree, Expected: [], Actual: {level_order(root1)}")
assert level_order(root1) == []

# Case 2: Single Node
root2 = TreeNode(1)
print(f"Case 2: Single Node, Expected: [[1]], Actual: {level_order(root2)}")
assert level_order(root2) == [[1]]

# Case 3: Simple Tree
root3 = TreeNode(1, TreeNode(2), TreeNode(3))
print(f"Case 3: Simple Tree, Expected: [[1], [2, 3]], Actual: {level_order(root3)}")
assert level_order(root3) == [[1], [2, 3]]

# PROBLEM 5

# 1. Share 2 questions you would ask to help understand the question:
#    What if tree is empty?
#    What does absolute difference mean? Does it mean we will have to calculate the difference based on absolute value of the nodes?

# 2. Write out in plain English what you want to do:
#    Utilize DFS to traverse the tree. Calculate the sum of left and right subtrees tilt.

# 3. Translate each sub-problem into pseudocode:
#    Create a helper function that will perform the DFS traversal
#    For main function, create a count for the tilt
#    Call helper function to perform DFS on the root of tree
#    return tilt

# 4. Translate the pseudocode into Python and share your final answer:

class TreeNode5:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def dfs(node, total_tilt):
  if not node:
      return 0

  left_sum = dfs(node.left, total_tilt)
  right_sum = dfs(node.right, total_tilt)

  tilt = abs(left_sum - right_sum)

  total_tilt[0] += tilt

  return node.val + left_sum + right_sum

def find_tilt(root):
  total_tilt = [0]
  dfs(root, total_tilt)
  return total_tilt[0]

# Case 1: Empty Tree
root1 = None
print(f"Case 1: Empty Tree, Expected: 0, Actual: {find_tilt(root1)}")
assert find_tilt(root1) == 0

# Case 2: Single Node
root2 = TreeNode5(1)
print(f"Case 2: Single Node, Expected: 0, Actual: {find_tilt(root2)}")
assert find_tilt(root2) == 0

# Case 3: Simple Tree
root3 = TreeNode5(1, TreeNode5(2), TreeNode5(3))
print(f"Case 3: Simple Tree, Expected: 1, Actual: {find_tilt(root3)}")
assert find_tilt(root3) == 1