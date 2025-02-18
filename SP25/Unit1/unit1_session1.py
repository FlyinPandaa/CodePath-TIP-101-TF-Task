# PROBLEM 1 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#       How do I print in Python?
#       Are there any time constraints I need to take into account?

# 2. Write out in plain English what you want to do:
#       Define the function and put print statement. Then call the function.

# 3. Translate each sub-problem into pseudocode:
#       Def function():
#           print()

#       call function

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

def hello_world():
    print("Hello World!")
    
hello_world()



# PROBLEM 2 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#       How do I change my mood?
#       Are there any time constraints I need to account for?

# 2. Write out in plain English what you want to do:
#       Change the mood to something else

# 3. Translate each sub-problem into pseudocode:
#       def function():
#           mood = change this
#           print(output)
#       call function()

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

def todays_mood():
    mood = "🥱"
    print("Today's mood: " + mood)

todays_mood()



# PROBLEM 6 [Version 1]

# 1. Share 2 questions you would ask to help understand the question:
#       How do I use an "If statment"?
#       What if the age is negative?

# 2. Write out in plain English what you want to do:
#       Create a function with if-else statments to determine if the person is "child" or "adult".

# 3. Translate each sub-problem into pseudocode:
#       def function():
#           if 18 or greater:
#               print(Adult)
#           else:
#               print(Child)

# 4. Translate the pseudocode into Python and share your final answer:

# Time Complexity: O(1)
# Space Complexity: O(1)

def classify_age(n):
    if n >= 18 and n >= 0:
        print("Adult")
    else:
        print("Child")

classify_age(18)



# PROBLEM 14 [Version 1]

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



# PROBLEM 15 [Version 1]

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


