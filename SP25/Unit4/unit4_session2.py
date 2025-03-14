# PROBLEM 1 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#       Will we ever have to check if the parameters are strings?
#       Will there be a limit to how long the typed string can be?

# 2. Write out in plain English what you want to do:
#       Use two-pointer to match characters from string 'name' and string 'typed'. If characters match, move both pointers. If they don't move pointer in the string 'typed' to check if the character is repeating.

# 3. Translate each sub-problem into pseudocode:
#    Declare two pointers
#    Loop through both strings check if characters match
#      if match:
#        increment both pointers
#      if no match:
#        only move pointer in typed
#      else:
#        mismatch return False
#    Account for all characters
#    Extra characters in string 'typed' is accounted for

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def is_long_pressed(name, typed):
  i, j = 0, 0

  while i < len(name) and j < len(typed):
    if name[i] == typed[j]:
      i += 1
      j += 1
    elif j > 0 or typed[j] == name[i]:
      j += 1
    else:
      return False

  if i < len(name):
    return False

  while j < len(typed):
    if typed[j] != name[-1]:
      return False

    j += 1

  return True
  pass

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))

# PROBLEM 2

# 1. Share 2 questions you would ask to help understand the question:
#       Will either or both the list be empty?
#       Are we guranteed the two lists will be equal in size?

# 2. Write out in plain English what you want to do:
#       Sort the two lists 'g' and 's'. Then find minimum value to satisfy the children.

# 3. Translate each sub-problem into pseudocode:
#    Sort list of greed factors and list of cookie sizes (use built-in sort function)
#    Initialize two pointers one for cookie the other for child
#    while child < len(g) and cookie < len(s):
#      if child is less than or equal to cookie:
#        child += 1
#      cookie += 1
#    return child value

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def find_content_children(g, s):
  g.sort()
  s.sort()

  child, cookie = 0, 0
  
  while child < len(g) and cookie < len(s):
    if g[child] <= s[cookie]:
      child += 1
    cookie += 1

  return child
  pass
  

g = [1,2,3]
s = [1,1,3]
print(find_content_children(g, s))

g = [1,1]
s = [2,2,2]
print(find_content_children(g, s))


# PROBLEM 3

# 1. Share 2 questions you would ask to help understand the question:
#       Will string 's' ever be empty?
#       Will this be similar to the other palindrome problem in session 1?

# 2. Write out in plain English what you want to do:
#       Compare characters from both ends using a helper function. If there is a mismatch try to remove either ends of the string to see if a palindrome can be formed.

# 3. Translate each sub-problem into pseudocode:
#    Helper function:
#      while left less than right:
#        if left value does not equal right value:
#          return False
#        increment left
#        decrement right
#      return True

#    main function:
#      initialize pointers
#      while left < right:
#        if s[left] != s[right]:
#          return helper(s, left + 1, right) or helper(s, left, right - 1)
#        increment left
#        decrement right
#      return True

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def helper(s, left, right):
  return all(s[k] == s[right - k + left] for k in range(left, right))

  # Second Solution
  # while left < right:
  #     if s[left] != s[right]:
  #         return False
  #     left += 1
  #     right -= 1
  # return True
      

def valid_palindrome(s):
  left = 0
  right = len(s) - 1

  while left < right:
    if s[left] != s[right]:
      return helper(s, left + 1, right) or helper(s, left, right - 1)
    left, right = left + 1, right - 1

  return True
  
  pass

s = "aba"
s2 = "abca"
s3 = "abc"

print(valid_palindrome(s))
print(valid_palindrome(s2))
print(valid_palindrome(s3))

# PROBLEM 4

# 1. Share 2 questions you would ask to help understand the question:
#       What if list is empty?
#       Will the list of integers include negative numbers?

# 2. Write out in plain English what you want to do:
#       Sort list of integers. Use two-pointer to find pairs that has the negative version of the other integer. Update the largest positive integer that has this property.

# 3. Translate each sub-problem into pseudocode:
#    nums.sort()
#    initialize two pointers
#    initialize largeK with -1
#    
#    while left < right:
#      sum = nums[left] + nums[right]
#    
#      if sum is too small or negative:
#        increment left
#      elif sum is too large:
#        decrement right
#      else: found a pair
#        largeK = nums[right]
#        left += 1
#        right -= 1
#    return largeK

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def find_largest_k(nums):
  nums.sort()
  left, right = 0, len(nums) - 1
  largeK = -1

  while left < right:
    sum = nums[left] + nums[right]

    if sum < 0:
      left += 1
    elif sum > 0:
      right -= 1
    else:
      largeK = nums[right]
      left += 1
      right -= 1

  return largeK
  pass

nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))

nums2 = [-10,2,7,-3]
print(find_largest_k(nums2))

# PROBLEM 5

# 1. Share 2 questions you would ask to help understand the question:
#       Will the string ever be empty?
#       Does the good substring have to be a length of 3 or can it be another length?

# 2. Write out in plain English what you want to do:
#       Use a fixed-window to loop through a window of 3 characters. Check if each character in a window is unique. If so, increment the count of good substrings found and return that value after the last window.

# 3. Translate each sub-problem into pseudocode:
#    initialize the count of good substrings
#    for i in range (len(s) - 2):
#      window = s[i:i+3]
#    check if all char in the window are unique
#      increment count
#    return count

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def count_good_substrings(s):
  res = 0

  for i in range(len(s) - 2):
    window = s[i:i+3]
    if len(window) == len(set(window)):
      res += 1

  return res
  pass

s1 = "xyzzaz"
s2 = "xyzxyz"
print(count_good_substrings(s1))
print(count_good_substrings(s2))