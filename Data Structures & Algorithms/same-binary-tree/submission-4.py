# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = collections.deque([p])
        q2 = collections.deque([q])
        while q1 and q2:
            # Inner loop not required as we're not concerned with level
            node1 = q1.popleft()
            node2 = q2.popleft()
            if not node1 and not node2:
                continue
            if node1 is None or node2 is None or node1.val != node2.val:
                return False

            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.left)
            q2.append(node2.right)
        return not q1 and not q2
        