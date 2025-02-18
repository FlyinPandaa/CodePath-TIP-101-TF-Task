# PROBLEM 1

# 1. Share 2 questions you would ask to help understand the question:
#    Do we need to account for a case where n is 0?
#    What would be the time complexity difference between the two methods.

# 2. Write out in plain English what you want to do:
#    Create a for loop to print hello while iteration is within "n" times.

# 3. Translate each sub-problem into pseudocode:
#    if n is empty:
#      return empty string
#    for i in range(n):
#      print Hello

# 4. Translate the pseudocode into Python and share your final answer:

# Recusrive solution has less lines of code 

# Time Complexity: O(n)
# Space Complexity: O(n)

def repeat_hello(n):
  if n > 0:
    print("Hello")
    repeat_hello(n - 1)

repeat_hello(5)

# Time Complexity: O(n)
# Space Complexity: O(1)

def repeat_hello_iterative(n):
  if n is None:
    return ""

  for _ in range(n):
    print("Hello")

print("with iterative:")

repeat_hello_iterative(5)
    

# PROBLEM 2

# 1. Share 2 questions you would ask to help understand the question:
#    What if there is no "n" input?
#    What if the "n" is negative?

# 2. Write out in plain English what you want to do:
#    If n is 0, then return 1
#    return n * function(n-1)

# 3. Translate each sub-problem into pseudocode:
#    if n == 0:
#      return 1
#    return n * function

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n-1)
  pass

n = 5

print(factorial(n))

# PROBLEM 3

# 1. Share 2 questions you would ask to help understand the question:
#    Is there a restriction or th time complexity?
#    What if the the lst is empty?

# 2. Write out in plain English what you want to do:
#    Iterate through the lst and add all numbers in the list

# 3. Translate each sub-problem into pseudocode:
#    if list is mpty:
#      return 0 
#    else:
#      return the sum of list recursively

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(n)
# Space complexity: O(n)

def sum_list(lst):
  if len(lst) == 0:
    return 0
  else:
    return lst[0] + sum_list(lst[1:])
  pass

lst = [1,2,3,4,5]
print(sum_list(lst))

# PROBLEM 4

# 1. Share 2 questions you would ask to help understand the question:
#    Do we need to account for when n = 0?
#    What if there are negative  value for "n"?

# 2. Write out in plain English what you want to do:
#    Recusively determine if a number is power of two by dividing "n" by two.

# 3. Translate each sub-problem into pseudocode:
#    if n is 1:
#      return true
#    elif n is greater than  1 or  n % 2 != 0:
#      return false
#    else: recursively return the function(n//2)

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(logn)
# Space complexity: O(logn)

def is_power_of_two(n):
  if n == 1:
    return True
  elif n < 1 or n % 2 != 0:
    return False
  else:
    return is_power_of_two(n//2)
  pass

print(is_power_of_two(6))

# PROBLEM 5

# 1. Share 2 questions you would ask to help understand the question:
#    What if the list is  only one element?
#    Can we use the search function?

# 2. Write out in plain English what you want to do:
#    Iterate through the "lst" and  find the targt value.

# 3. Translate each sub-problem into pseudocode:
#    Declare the two pointers
#    while left and right did not cross:
#      delcare mid
#      if middle == target
#        return mid
#      elif lst[mid] > target:
#        right = mid - 1
#      else:
#        left = mid + 1
#    return -1 if target value can't be found

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(logn)
# Space complexity: O(1)

def binary_search(lst, target):
  left, right = 0, len(lst) - 1

  while left <= right:
    mid = (left + right) // 2

    if lst[mid] == target:
      return mid
    elif lst[mid] > target:
      right = mid - 1
    else:
      left = mid + 1

  return -1
  pass

lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11

print(binary_search(lst, target))