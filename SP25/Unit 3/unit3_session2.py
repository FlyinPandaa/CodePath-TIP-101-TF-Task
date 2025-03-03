# PROBLEM 1 [Version 2]

# 1. Share 2 questions you would ask to help understand the question:
#       Is there a Python function that helps with turning string to integer?
#       What if the we aren't provided a string?

# 2. Write out in plain English what you want to do:
#       Loop through string and convert each character into an integer.

# 3. Translate each sub-problem into pseudocode:
#       initialize result list
#       for characters in s:
#           integer_value = convert_to_integer(character)
#           result_list = result_list.append(integer_value)
#       return result_list

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity:
# Space Complexity:

def string_to_integer_mapping(s):
    res = []
    
    for character in s:
        integer_value = int(character)
        res.append(integer_value)
        
    return res

print(string_to_integer_mapping("12345"))  # Output: [1, 2, 3, 4, 5]
print(string_to_integer_mapping("908"))    # Output: [9, 0, 8]
print(string_to_integer_mapping("0"))      # Output: [0]

# PROBLEM 2 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#       Will the input list be empty?
#       Do we need to account for the time complexity of the sorting the list of integers?

# 2. Write out in plain English what you want to do:
#       Loop through list and find and remove duplicates.

# 3. Translate each sub-problem into pseudocode:
#       if list is empty: return empty list
#       set a counter to 0
#       while the tracker i < len(nums)-1:
#           if integer at current is same as next integer remove duplicate
#           else increase i to move to next index
#       return nums

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def remove_duplicates(nums):
  if not nums:
    return []
  i = 0

  while i < len(nums)-1:
    if nums[i] == nums[i+1]:
      nums.pop(i)
    else:
      i += 1
  return nums
  pass

nums = [1,1,1,2,3,4,4,5,6,6]

print(remove_duplicates(nums))

# PROBLEM 3 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#       Will the string be empty?
#       What if the string is just integers?

# 2. Write out in plain English what you want to do:
#       List out letters in the string and reverse the new string.

# 3. Translate each sub-problem into pseudocode:
#       letters = []
#       for char in s:
#           if char.isalpha():
#               letters.append(char)

#       res = ""
#       l_index = len(letters) - 1

#       for charcters in string s:
#           check if characters are part of the alphabet:
#               res += letters[l_index]
#               decrement l_index
#           otherwise add char to res

#       return res

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def reverse_only_letters(s):
    letters = []
    
    for char in s:
        if char.isalpha():
            letters.append(char)

    result = ""
    l_index = len(letters) - 1

    for char in s:
        if char.isalpha():
            result += letters[l_index]
            l_index -= 1
        else:
            result += char
    return result

pass

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)

# PROBLEM 4 [Version #]

# 1. Share 2 questions you would ask to help understand the question:
#       Will the input ever be empty?
#       Is there a limit to how many repeated letters in an input?

# 2. Write out in plain English what you want to do:
#    Loop through the input string and track longest sequence of the same characters in a row.

# 3. Translate each sub-problem into pseudocode:
#       if not s: return 0
#       max_length = 1
#       curr_length = 1
#       for i in range of the length of string s:
#           if s[i] == s[i-1]:
#               curr_length += 1
#               update max_length
#           else:
#               curr_length = 1
#       return max+length

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def longest_uniform_substring(s):
  if not s:
      return 0
    
  max_length = 1
  curr_length = 1
  
  for i in range(1, len(s)):
      if s[i] == s[i-1]:
          curr_length += 1
          max_length = max(max_length, curr_length)
      else:
          curr_length = 1
  return max_length

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l1 = longest_uniform_substring(s2)
print(l1)

# PROBLEM 5 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#       Is there a limit to how long the still poisoined state can last?
#       Will we need a time function for this question?

# 2. Write out in plain English what you want to do:
#       For each attack, check if the duration is interrupted by another attack, and add up the actual duration of each poison effect.

# 3. Translate each sub-problem into pseudocode:
#       Create empty list.
#       for each attack:
#           actual duration is smaller:
#               the duration input
#               the next attack minus time of attack
#       total_duration increment by duration
#       reutrn total

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def find_poisoned_duration(time_series, duration):
  total_duration = 0
  
  for i in range(len(time_series)-1):
      actual_duration = min(time_series[i+1] - time_series[i], duration)
      total_duration += actual_duration
    
  total_duration += duration
  
  return total_duration

time_series = [1,4,9]
damage = find_poisoned_duration(time_series, 3)
print(damage)

