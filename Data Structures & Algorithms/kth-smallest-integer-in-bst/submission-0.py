# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        answer = None

        def df(root):
            nonlocal answer, count
            if not root or count == 0:
                return
            df(root.left)
            count -= 1
            if count == 0:
                answer = root.val
                return
            df(root.right)
        df(root)
        return answer

        