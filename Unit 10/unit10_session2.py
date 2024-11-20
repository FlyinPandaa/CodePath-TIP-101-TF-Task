# PROBLEM 1

# 1. Share 2 questions you would ask to help understand the question:
#    What if the 'nums' array is empty?
#    Will all integers be positive?

# 2. Write out in plain English what you want to do:
#    Use hashing to keep track of integers we have seen. Set to return True when finding an integer. If  end of loop and no same integers were encountered, return false.

# 3. Translate each sub-problem into pseudocode:
#    Create empty hash set
#    Loop through the integers in the array:
#      If integer is seen in the set: return True
#      Else add the integer to the set
#    return false if loop doesn't find duplicates

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n) - Has to iterate through each integer in the array
# Space Complexity: O(n) - need additional space for set.

def contains_duplicate(nums):
  seen = set()
  
  for i in nums:
      if i in seen:
          return True
      seen.add(i)
    
  return False

print(contains_duplicate([1, 2, 3, 4]))

print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

print(contains_duplicate([]))

# PROBLEM 2

# 1. Share 2 questions you would ask to help understand the question:
#    What if the list of integers is empty?
#    What does "in-place" mean?

# 2. Write out in plain English what you want to do:
#    Utilize a pointer to keep track of current position. Replace elements that are not equal to the target value. Increment pointer.

# 3. Translate each sub-problem into pseudocode:
#    Initialize pointer
#    Loop through each element in the array
#      if the current element is  not equal to val
#        replace the current with the nums(i)
#        increment pointer
#    return the pointer

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n) - Need to traverse the array
# Space Complexity: O(1) - Only need constant space

def remove_element(nums, val):
  k = 0
  
  for i in range(len(nums)):
      if nums[i] != val:
          nums[k] = nums[i]
          k += 1
        
  return k

# Test Case #1
nums1 = [3, 2, 2, 3]
val1 = 3

print(remove_element(nums1, val1)) # Output: 2
print(nums1) # Output: [2, 2, 3, 3]

# Test Case #2
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2

print(remove_element(nums2, val2)) # Output: 5
print(nums2) # Output: [0, 1, 4, 0, 3, 2, 2, 2]

# Test Case #3
nums3 = [1, 1]
val3 = 1

print(remove_element(nums3, val3)) # Output: 0
print(nums3) # Output: [1, 1]

# PROBLEM 3

# 1. Share 2 questions you would ask to help understand the question:
#    What if one or both strings are empty?
#    What if there is no GCD for a test case?

# 2. Write out in plain English what you want to do:
#    Use GCD of the lengths of the strings and find the largest divisor string. Check if the string divides string 1 and string 2.

# 3. Translate each sub-problem into pseudocode:
#    Create a helper that checks if string can be divisible
#    Find the GCD of string 1  and 2
#    Use the GCD length to get a possible divisor
#    Check if the substring can divide both string 1 and 2
#    If can divide both string: return the substring
#    If not return empty string

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n) - Need to traverse both strings
# Space Complexity: O(1) - No additional space needed

def gcd_of_strings(str1, str2):
  def is_divisible(s, t):
      if len(s) % len(t) != 0:
          return False
      repeat = len(s) // len(t)
      return t * repeat == s

  def gcd(a, b):
      while b:
          a, b = b, a % b
      return a

  gcd_length = gcd(len(str1), len(str2))
  candidate = str1[:gcd_length]

  if is_divisible(str1, candidate) and is_divisible(str2, candidate):
      return candidate
  return ""

print(gcd_of_strings("ABCABC", "ABC")) # Output: ABC

print(gcd_of_strings("ABABAB", "ABAB")) # Output: AB

print(gcd_of_strings("LEET", "CODE")) # Output: ""

# PROBLEM 4

# 1. Share 2 questions you would ask to help understand the question:
#    What if the tree is empty?
#    What if one tree only goes down one side of the tree?

# 2. Write out in plain English what you want to do:
#    Utilize recursion to check if the tree is balanced or not by checking if the left or right subtree's height difference is not more than 1.

# 3. Translate each sub-problem into pseudocode:
#    Define a helper function that checks the balance and height of the tree
#    Call helper function to check if tree is balanced
#    Return if the tree is balanced or not

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n) - Has to visit each node
# Space Complexity: O(n) - Need additional space based on size of tree

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
    
def check_balance_and_height(node):
  if not node:
      return True, 0
    
  left_balanced, left_height = check_balance_and_height(node.left)
  right_balanced, right_height = check_balance_and_height(node.right)
  
  # Check for imbalance immediately
  if not left_balanced or not right_balanced or abs(left_height - right_height) > 1:
      return False, 0  # Return False and a dummy height
    
  height = max(left_height, right_height) + 1
  
  return True, height
  
def is_balanced(root):
  balanced, height = check_balance_and_height(root)
  return balanced

# Test Case 1: Balanced Tree
tree1 = TreeNode(1,
               TreeNode(2,
                       TreeNode(4),
                       TreeNode(5)),
               TreeNode(3,
                       TreeNode(6),
                       TreeNode(7)))
print(is_balanced(tree1))  # Output: True

# Test Case 2: Unbalanced Tree
tree2 = TreeNode(1,
               TreeNode(2,
                       TreeNode(4),
                       TreeNode(5)),
               TreeNode(3,
                       TreeNode(6)))
print(is_balanced(tree2))  # Output: False

# Test Case 3: Empty Tree
tree3 = None
print(is_balanced(tree3))  # Output: True

# PROBLEM 5

# 1. Share 2 questions you would ask to help understand the question:
#    What if array is empty?
#    Are there any time or space constraints?

# 2. Write out in plain English what you want to do:
#    Use hash map to store the the sum and frequency of the elements. Loop through the array, and for each element check i the sum - k is in the hash map. If it exists add the frequency of the sum to count. Update the hash map with the current sum.

# 3. Translate each sub-problem into pseudocode:
#    Create hash map and initialize counters
#    Loop through each element num in the array:
#      Add num to current sum
#      If current sum is = to k; count += 1
#      if the current sum = k exists in the hash map
#      Update sum with current sum
#    return the count

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n) - Need to loop through array
# Space Complexity: O(n) - need additional space

def subarray_sum(nums, k):
  cumulative_sum = {0: 1}
  current_sum = 0
  count = 0
  for num in nums:
      current_sum += num
      if current_sum == k:
          count += 1
      if current_sum - k in cumulative_sum:
          count += cumulative_sum[current_sum - k]
        
      # Update cumulative_sum after incrementing count
      if current_sum in cumulative_sum:
          cumulative_sum[current_sum] += 1
      else:
          cumulative_sum[current_sum] = 1
  return count

print(subarray_sum([1, 1, 1], 2)) # Output: 2

print(subarray_sum([1, 2, 3], 3)) # Output: 2

print(subarray_sum([1, 2, 1, 2, 1], 3)) # Output: 4
