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