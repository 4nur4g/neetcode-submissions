# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0
        def dm(node):
            nonlocal diam
            if not node:
                return 0
            left_height = dm(node.left)
            right_height = dm(node.right)

            diam = max(diam, left_height + right_height)
            # Height of current node
            return 1 + max(left_height, right_height)
        dm(root)
        return diam
        