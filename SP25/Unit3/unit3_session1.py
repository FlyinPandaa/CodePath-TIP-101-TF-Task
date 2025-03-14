# PROBLEM 1 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#       What happens when we set limits to 0?
#       What if we are provided no input?

# 2. Write out in plain English what you want to do:
#       Below the function we will print out the while passing in a value to assign to limits.

# 3. Translate each sub-problem into pseudocode:
#       print(function(# - some value))

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def count_mississippi(limit):
  for num in range(1, limit):
    print( f"{num} mississippi")

print(count_mississippi(6))


# PROBLEM 2 [Version 2]

# 1. Share 2 questions you would ask to help understand the question:
#       What if we aren't given the parameters `s` and `n`?
#       Would I use a for loop for this question?

# 2. Write out in plain English what you want to do:
#       Loop through string `s` and go to index `n`. Remove character and return new string `s`

# 3. Translate each sub-problem into pseudocode:
#       if n is >= 0 or n <= len(s):
#           return "invalid input"

#       new_string = s remove index n
#       return string

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

def remove_char(s, n):
    if n <= 0 or n >= len(s):
        return "invalid input"
    
    new_string = s[:n] + s[n+1:]
    
    return new_string

s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)

# PROBLEM 2 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#       Will we need to account for empty strings?
#       Will there be a case where we need to swap the ends back to the original?

# 2. Write out in plain English what you want to do:
#       Slice the string into parts and then comebine them together.

# 3. Translate each sub-problem into pseudocode:
#       my_str[-1:]
#       my_str[1:-1]
#       my_str[:1]
#       Return combined string

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

def swap_ends(my_str):
  return my_str[-1:] + my_str[1:-1] + my_str[:1]
  pass

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)

# PROBLEM 3 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#       What if the string is empty?
#       Can there be repeats of the same letter?

# 2. Write out in plain English what you want to do:
#       Loop through the string and check if every letter in the alphabet is in the string.

# 3. Translate each sub-problem into pseudocode:
#       alphabet = "abcdefg ..."
#       for i in alphabet:
#           if i is not in the string:
#               return False
#       otherwise return True

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def is_pangram(my_str):
  alphabet = "abcdefghijklmnopqrstuvwxyz"

  for i in alphabet:
    if i not in my_str.lower():
      return False
      
  return True
  pass

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))


# PROBLEM 4 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#       Do we need to account for an empty string?
#       Is there a limit to the size of the string?

# 2. Write out in plain English what you want to do:
#       Slice the string in reverse order.

# 3. Translate each sub-problem into pseudocode:
#       reversed_str = ""
#       for i in my_str:
#           reverse string
#       return reversed_string

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def reverse_string(my_str):
  rev_string = ""

  for i in my_str:
    rev_string = i + rev_string

  return rev_string
  pass

my_str = "live"
print(reverse_string(my_str))

