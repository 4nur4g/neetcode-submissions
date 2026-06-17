# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def df(root,p,q):
            if not root:
                return
            if p.val > root.val and q.val > root.val:
                return df(root.right, p, q)
            if p.val < root.val and q.val < root.val:
                return df(root.left, p, q)
            else:
                return root
        return df(root,p,q)
        