# UPI steps

# Understand:



# Plan



#Implement

def reverse_list(lst):
  left = 0
  right = len(lst) - 1

  while left < right:
    # Line 19 - 22 // Swap
    temp = lst[left]
    lst[left] = lst[right]
    lst[right] = temp

    left += 1
    right -= 1

  return lst
  pass

lst = [1, 2, 3, 4, 5]
print(lst)
print(reverse_list(lst))



def is_prime(n):
    # if i < 2 its not prime number
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime(5))
print(is_prime(12))
print(is_prime(9))






def modify_list(lst):
    lst.append(100)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 100]


def modify_number(n):
    n += 1

my_number = 10
modify_number(my_number)
print(my_number)  # Output: 10


def modify_value(pointer):
    pointer[0] += 1  # Modify the first element

my_value = [10]  # A list that contains an integer
modify_value(my_value)
print(my_value[0])  # Output: 11


i = 0
j = len(my_value) - 1