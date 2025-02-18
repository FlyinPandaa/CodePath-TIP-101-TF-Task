# Set 1

# PROBLEM 14

# 1. Share 2 questions you would ask to help understand the question:
#    Will we be given empty inputs?
#    Will both the start and stop value be positive?

# 2. Write out in plain English what you want to do:
#    Create variable to store total
#    Loop through the values
#    Return the total value

# 3. Translate each sub-problem into pseudocode:
#    res = 0
#    for loop to go through all values:
#       add the number to the res
#    return res

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def sum_range(start, stop):
	res = 0
 
	for num in range (start, stop + 1):
		res += num
	return res

# PROBLEM 15

# 1. Share 2 questions you would ask to help understand the question:
#    Will the list contain both negative and positive numbers?
#    Is there a limit to how many negative numbers there are?

# 2. Write out in plain English what you want to do:
#    Loop through all numbers in the list
#    If num < 0 : print(num)

# 3. Translate each sub-problem into pseudocode:
#    loop through list:
#       if num < 0: print(num)

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def print_negatives(lst):
    for num in lst:
        if num < 0:
            print(num)
            

# Set 2

# PROBLEM 14

# 1. Share 2 questions you would ask to help understand the question:
#    Can the multiplier be negative?
#    Is there a limit to the size of the list?

# 2. Write out in plain English what you want to do:
#    Create an empty list
#    Loop through list, and append th multiplied value
#    Return the populated list

# 3. Translate each sub-problem into pseudocode:
#    res = []
#    Loop through list: append
#    return res

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(n)

def multiply_list(lst, multiplier):
	res = []
 
	for num in lst:
		res.append(num * multiplier)
  
	return res

# PROBLEM 15

# 1. Share 2 questions you would ask to help understand the question:
#    Will there be negative values in the list?
#    Is there a time complexity constraint?

# 2. Write out in plain English what you want to do:
#    Create count variable
#    Loop through list:
#       Check number if it's an even or odd
#       If even: increment count
#    return count

# 3. Translate each sub-problem into pseudocode:
#    count = 0
#    loop through list:
#       Find even numbers: increment count

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity:
# Space Complexity:

def count_evens(lst):
	count = 0
 
	for num in lst:
		if num % 2 == 0:
			count += 1
   
	return count