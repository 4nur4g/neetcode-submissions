# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maximum):
            if not root:  
                return 0
            count = 0 if maximum and maximum.val > root.val else 1
            maximum = max([maximum, root], key = lambda x: x.val if x else float('-inf'))
            count += dfs(root.left, maximum)
            count += dfs(root.right, maximum)
            return count

        return dfs(root, None)


