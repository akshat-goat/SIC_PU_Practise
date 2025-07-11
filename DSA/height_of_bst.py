class TreeNode:
    def __init__(self, x):
        self.x = x
        self.L = None
        self.R = None

def height(root: TreeNode) -> int:
    if root is None:
        return -1
    
    left_subtree_height = height(root.L)
    
    right_subtree_height = height(root.R)
    
    return 1 + max(left_subtree_height, right_subtree_height)

