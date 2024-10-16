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