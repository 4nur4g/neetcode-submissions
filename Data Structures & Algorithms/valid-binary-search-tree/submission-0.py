# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maximum = float('-inf')
        minimum = float('inf')
        def ds(root,left,right):

            if not root:
                return True
            if  not (left < root.val < right):
                return False

            return ds(root.left, left, root.val) and ds(root.right, root.val, right)

        return ds(root, maximum, minimum)
        