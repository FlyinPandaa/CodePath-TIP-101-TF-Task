def binary_search(lst, target):
    # Initialize a left pointer to the 0th index in the list
    left = 0
    # Initialize a right pointer to the last index in the list
    right = len(lst)-1
    
    # While left pointer is less than right pointer:
    while left < right:
        # Find the middle index of the array
        mid = (right + left)//2
        # If the value at the middle index is the target value:
        if lst[mid] == target:
            # Return the middle index
            return mid
        # Else if the value at the middle index is less than our target value:
        elif lst[mid] < target:
            # Update pointer(s) to only search right half of the list in next loop iteration
            left = mid + 1
        # Else
        else:
            # Update pointer(s) to only search left half of the list in next loop iteration
            right = mid - 1
    # If we search whole list and haven't found target value, return -1
    return -1

lst = [1,2,3,4,5]
target = 6

print(binary_search(lst, target))