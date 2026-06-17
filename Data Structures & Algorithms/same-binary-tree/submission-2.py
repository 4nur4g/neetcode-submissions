# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def ds(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            left = ds(p.left, q.left)
            right = ds(p.right, q.right)

            condition = p.val == q.val and left and right

            return condition
        return ds(p,q)

        