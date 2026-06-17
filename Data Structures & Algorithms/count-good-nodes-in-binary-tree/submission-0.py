# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def ds(root, maximum):
            nonlocal count
            if not root:
                return 0
            if root.val >= maximum:
                count += 1
            maximum = max(maximum, root.val)
            ds(root.left, maximum)
            ds(root.right, maximum)
        ds(root,root.val)
        return count
            



       


        