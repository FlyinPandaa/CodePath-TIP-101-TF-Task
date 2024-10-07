# PROBLEM 1

# 1. Share 2 questions you would ask to help understand the question:
#    What if n is negative?
#    What if non-prime number returns less than 2?

# 2. Write out in plain English what you want to do:
#    First check if n is less than 2.
#    Check factors of 2 up until square root of n.

# 3. Translate each sub-problem into pseudocode:
#    if n <= 1:
#      return false
#    set i = 2
#    while i * i <= n:
#      if n % i == 0:
#        return False
#       otherwise increment i by 1
#    return true

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)


def is_prime(n):
  if n <= 1:
    return False

  i = 2

  while i * i <= n:
    if n % i == 0:
      return False
    i += 1

  return True
  pass


print(is_prime(5))
print(is_prime(12))
print(is_prime(9))

# PROBLEM 2

# 1. Share 2 questions you would ask to help understand the question:
#    What if the list is empty?
#    What does "in-place" mean?

# 2. Write out in plain English what you want to do:
#    Utilize the two pointer method to start from the end of the list and beginning of the list to reverse list.

# 3. Translate each sub-problem into pseudocode:
#    Initialize the two pointers left and right
#    while left < right:
#      swap elements
#      increment left pointer
#      decrement right pointer
#    return the list

# 4. Translate the pseudocode into Python and share your final answer:\
# Time Complexity: O(n)
# Space Complexity: O(1)

def reverse_list(lst):
  left = 0
  right = len(lst) - 1

  while left < right:
    temp = lst[left]
    lst[left] = lst[right]
    lst[right] = temp

    left += 1
    right -= 1

  return lst
  pass

lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))


# PROBLEM 3

# 1. Share 2 questions you would ask to help understand the question:
#    What is time and space complexity?
#    Which method is faster? Two pointer or slicing?

# 2. Write out in plain English what you want to do:
#    Analyze the two different codes to come up with the time and space complexity of both methods of reversing a list.

# 3. Translate each sub-problem into pseudocode:
#    Two pointer: 
#      time:
#      space:
#    Slicing:
#      time:
#      space:

# 4. Translate the pseudocode into Python and share your final answer:
#    Two pointer: 
#      time: O(n) - Same time complexity.
#      space: O(1)- More efficient use of space.
#    Slicing:
#      time: O(n) - Same time complexity.
#      space: O(n) - Requires additional space to reverse list.

# Time Complexity: O(n)
# Space Complexity: O(1)

def pointer_reverse_list(lst):
  left = 0
  right = len(lst) - 1

  while left < right:
    temp = lst[left]
    lst[left] = lst[right]
    lst[right] = temp

    left += 1
    right -= 1

  return lst

def non_pointer_reverse_list(lst):
  # Create a new reversed list
  reversed_lst = lst[::-1]
  # Copy the elements back into the original list
  for i in range(len(lst)):
      lst[i] = reversed_lst[i]



# PROBLEM 4

# 1. Share 2 questions you would ask to help understand the question:
#    What happens if all numbers are even?
#    Will the input list ever be empty?

# 2. Write out in plain English what you want to do:
#    Use two-pointer method to separate even and odd numbers into two lists.

# 3. Translate each sub-problem into pseudocode:
#    Initialize two pointers 'left' and 'right'
#    while left < right:
#      if even: increment left pointer
#      else if odd: decrement right pointer
#      else: swap left pointer to odd number and right pointer to even number

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def sort_array_by_parity(nums):
  left = 0
  right = len(nums) - 1

  while left < right:
    # Even
    if nums[left] % 2 == 0:
      left += 1
    # Odd
    elif nums[right] % 2 != 0:
      right -= 1
    # Swap
    else:
      nums[left], nums[right] = nums[right], nums[left]
      left += 1
      right -= 1
      
  return nums
  pass

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

# PROBLEM 5

# 1. Share 2 questions you would ask to help understand the question:
#    What if the list of strings  is empty?
#    Will the solution have to take into account integers being mixed in with the string?

# 2. Write out in plain English what you want to do:
#    Utilize a helper function to look at each string in the list and return the string that is a palindrome. If none, return an empty string.

# 3. Translate each sub-problem into pseudocode:
#    Helper function:
#      initialize left and right pointer
#      While left < right:
#        if left pointer not equal to right pointer:
#          return False
#        increment left pointer
#        decrement right pointer
#      return True if reach end of function
#
#    Main function:
#      for i in words:
#        if is Helper function:
#          return i
#      return empty string if no palindrome

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def helper(s):
  left = 0 
  right = len(s) - 1

  while left < right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1

  return True

def first_palindrome(words):
  for i in words:
    if helper(i):
      return i
      
  return ""
  pass

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)

