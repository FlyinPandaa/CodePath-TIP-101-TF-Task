def remove_tail(head):
    # Initialize previous, that will keep track of the node before current node
    previous = None
    
    # If an empty linked list is passed into the function, return none (null)
    if head is None: 
        return None
    
    # If there is only one node in the linked list, return none
    if head.next is None: 
        return None 
    
    # Start at beginning of linked list
    current = head
    
    # While there is a next node in the list, continue looping
    while current.next:
    
        # Set 'previous' to the current node
        # This saves the current node as 'previous', before moving 'current' to the next node
        previous = current
        
        # Move 'current' to the next node in the list
        # 'current' will now point to the next node (the one after the current node)
        current = current.next

        
    # Set the pointer to point to None
    previous.next = current.next
    
    # Current to none (basiccally clean up or delete the old tail node)
    current = None
    
    # Return linked list
    return head