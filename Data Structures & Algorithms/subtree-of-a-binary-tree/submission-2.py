# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        return self.checkSubtree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    @staticmethod 
    def checkSubtree(root: TreeNode, subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None or root.val != subRoot.val:
            return False
        return  Solution.checkSubtree(root.left, subRoot.left) and Solution.checkSubtree(root.right, subRoot.right)

        
        