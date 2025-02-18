# PROBLEM 10 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#       What if "n" is negative?
#       Are there any time constraints that I need to follow?

# 2. Write out in plain English what you want to do:
#       Create a function that takes in an input "n". Use mod operator to determine output.

# 3. Translate each sub-problem into pseudocode:
#       def function(n):
#           if(n % 3 == 0):
#               print("Fizz")
#           elif(n % 5 == 0):
#               print("Buzz")
#           else:
#               print(n)


# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

def fizzbuzz(n):
    if(n % 3 == 0):
        print("Fizz")
    elif(n % 5 == 0):
        print("Buzz")
    else:
        print(n)

fizzbuzz(11)


# PROBLEM 11 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#       Can list be empty?
#       Will the list contain negative numbers?

# 2. Write out in plain English what you want to do:
#       Loop through list
#       Print index

# 3. Translate each sub-problem into pseudocode:
#       for i in range(len(lst)): print(index)

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def print_indices(lst):
    for i in range(len(lst)):
        print(i)
        
    pass

# PROBLEM 12 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#       Does the value being negative or postiive matter?
#       Are we guranteed all values in the list are unique?

# 2. Write out in plain English what you want to do:
#       Loop through list to  ind the index of a target value

# 3. Translate each sub-problem into pseudocode:
#       Loop through list:
#           if the lst[i] == target:
#               return i
#       otherwise return -1    

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1



# PROBLEM 11 [Version 2]

# 1. Share 2 questions you would ask to help understand the question:
#       Does the nums being postiive or negative matter?
#       What are  the two possible ways that you can work on the new stuff

# 2. Write out in plain English what you want to do:
#       Loop through the list and find the value at each odd index

# 3. Translate each sub-problem into pseudocode:
#       Loop through the list:
#           ind odd res by using this line of code: i % 2 == 1
#           print the values at odd res

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def print_indices(lst):
	for i in range(len(lst)):
		if i % 2 == 1:
			print(lst[i])


# PROBLEM 12 [Version 2]

# 1. Share 2 questions you would ask to help understand the question:
#       Will we be guranteed positive numbers?
#       Is there a limit to repeat numbers?

# 2. Write out in plain English what you want to do:
#       Loop through the list, and if element  at correct index, add index to res

# 3. Translate each sub-problem into pseudocode:
#       res = []

#       Loop through list: append when index matches target
#       return res

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(n)
# Space Complexity: O(1)

def find_all_occurrences(lst, target):
    res = []
    
    for i in range(len(lst)):
        if lst[i] == target:
            res.append(i)
            
    return res


