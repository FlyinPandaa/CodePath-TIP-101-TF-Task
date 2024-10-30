# PROBLEM 1

# 1. Share 2 questions you would ask to help understand the question:
#    What if the input is empty?
#    How much time does it take

# 2. Write out in plain English what you want to do:
#    Recursively validate if the parantheses are nested.

# 3. Translate each sub-problem into pseudocode:
#    If string is empty, return true
#    if length of s >= 2 and s[0] == either '(' or ')':
#      return function(s[1:-1])
#    return False

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(n)
# Space complexity: O(n)

def is_nested(paren_s):
  if paren_s == "":
    return True

  if len(paren_s) >= 2 and paren_s[0] == '(' and paren_s[-1] == ')':
    return is_nested(paren_s[1:-1])
  return False
  pass

paren_s = (())

print(is_nested(paren_s))

# PROBLEM 2

# 1. Share 2 questions you would ask to help understand the question:
#    What if the list is empty?
#    Will we have cases where the entire list will be 1s?

# 2. Write out in plain English what you want to do:
#    Use binary search to find where the 1s begin, and count from there.

# 3. Translate each sub-problem into pseudocode:
#    declare two pointers
#    Find the middle using a while loop
#    if low < len(lst) and lst[low] == 1:
#      return the length of list - low

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(logn)
# Space complexity: O(1)

def count_ones(lst):
  low, high = 0, len(lst) - 1
  
  while low <= high:
      mid = (low + high) // 2
    
      if lst[mid] == 0:
          low = mid + 1
      else:
          high = mid - 1

  if low < len(lst) and lst[low] == 1:
      return len(lst) - low
    
  return 0
  pass

lst = [0, 0, 0, 0, 1, 1, 1]
print(count_ones(lst))

# PROBLEM 3

# 1. Share 2 questions you would ask to help understand the question:
#    Are we guranteed  to always have a target value?
#    What if the list is empty?

# 2. Write out in plain English what you want to do:
#    Recursively go through list and search for target value.

# 3. Translate each sub-problem into pseudocode:
#    If target not found: return -1
#    calculate middle
#    
#    If target found: return mid
#    
#    if target < nums[mid]
#      Search left
#    else:
#      serach right
#    
#    def binary search recursive function
#    return binary search

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(n)
# Space complexity: O(n)

def binary_search(nums, target):
  left, right = 0, len(nums) - 1
  if left > right:
    return -1  
    
  mid = (left + right) // 2
  
  if nums[mid] == target:
    return mid
  
  if target < nums[mid]:
    
    result = binary_search(nums[left:mid], target)
    
    if result != -1:
      return result + left 
    else:
      return -1
      
  else:
    result = binary_search(nums[mid+1:right+1], target)
    
    if result != -1:
      return result + (mid + 1) # Add (mid + 1) to get the correct index
    else:
      return -1
  pass
  
def binary_search_recursive(nums, target):
  return binary_search(nums, target)

nums = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11

print(binary_search_recursive(nums, target))

# PROBLEM 4

# 1. Share 2 questions you would ask to help understand the question:
#    What if nums is empty?
#    What is a circular linked list?

# 2. Write out in plain English what you want to do:
#    Binary search to find index of min element.

# 3. Translate each sub-problem into pseudocode:
#    declare pointers
#    While low <= high: search the array
#    Determine if mid element is min element
#    return 0 if reach the end

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(logn)
# Space complexity: O(1)

def count_rotations(nums):
  low, high = 0, len(nums) - 1
  
  while low <= high:
      if nums[low] <= nums[high]:
          return low
      mid = (low + high) // 2
      next_index = (mid + 1) % len(nums) 
      prev_index = (mid - 1 + len(nums)) % len(nums) 

      
      if nums[mid] <= nums[next_index] and nums[mid] <= nums[prev_index]:
          return mid
      elif nums[mid] > nums[high]:
          low = mid + 1  
      else:
          high = mid - 1

  return 0
  pass

nums = [8, 9, 10, 2, 5, 6]

print(count_rotations(nums))

# PROBLEM 5

# 1. Share 2 questions you would ask to help understand the question:
#    What if lst is empty?
#    Are there time restrictions for the time complexity?

# 2. Write out in plain English what you want to do:
#    Recursively split the list into havles until sublists are somewhat sorted, then merger the sublist back.

# 3. Translate each sub-problem into pseudocode:
#    

# 4. Translate the pseudocode into Python and share your final answer:

# Time complexity: O(nlogn)
# Space complexity: O(n)

# Helper function: Merges two sorted lists into one sorted list
def merge(left, right):
  result = [] # List to store the merged result
  i = j = 0 # Pointers to iterate over left and right input arrays

  # Compare elements from left and right halves of the list and add them to the
  # result list in the correct order
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1
  # Add any remaining elements from the left half to the result list
  while i < len(left):
      result.append(left[i])
      i += 1

  # Add any remaining elements from the right half to the result list
  while j < len(right):
      result.append(right[j])
      j += 1

  return result

def merge_sort(lst):
  if len(lst) <= 1:
    return lst

  mid = len(lst) // 2
  left_half = lst[:mid]
  right_half = lst[mid:]

  # Recursive calls to merge_sort for sorting the left and right halves
  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)

  return merge(left_half, right_half)
  pass

lst = [5,3,4,2,1]

print(merge_sort(lst))