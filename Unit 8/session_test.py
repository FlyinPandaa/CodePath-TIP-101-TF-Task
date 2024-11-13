class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_univalued(root):
    if not root:
        return True

    val = root.val

    def dfs(node, val):
        # If node is None, return True because an empty subtree is univalued
        if not node:
            return True
        # If the current node's value does not match, return False
        if node.val != val:
            return False
        # Recursively check left and right subtrees
        return dfs(node.left, val) and dfs(node.right, val)

    return dfs(root, val)

# Test with sample tree
n1 = TreeNode(1)
n2 = TreeNode(1)
n3 = TreeNode(1)
n4 = TreeNode(2)
n5 = TreeNode(1)
n6 = TreeNode(1)

n1.left = n2
n2.left = n3
n2.right = n6
n1.right = n4
n4.right = n5

print(is_univalued(n1))  # Expected output: False (since node n5 has a different value)