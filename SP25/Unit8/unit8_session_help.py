# Student solution Unit 8 Session 2 Problem #1 [Version 1] 

class TreeNode():
   def __init__(self, value, left=None, right=None):
       self.val = value

       self.left = left
       self.right = right

def is_univalued(root):
    pointer = root
    
    if pointer.lef and pointer.right:
        if pointer.lft.val == pointer.val and pointer.right.val == pointer.val:
            return is_univalued(pointer.left) and is_univalued(pointer.right)
        else:
            return False
    elif pointer.left:
        if pointer.left.val == pointer.val:
            return is_univalued(pointer.left)
        else:
            return False
    elif pointer.right:
        if pointer.right.val == pointer.val:
            return is_univalued(pointer.right)
        else:
            return False
    else:
        return True
    

    