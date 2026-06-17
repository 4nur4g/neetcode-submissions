# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def df(preorder, inorder):
            if not preorder or not inorder:
                return None

            currentNode = TreeNode(preorder[0])         
            mid = inorder.index(preorder[0])

            inorderLeft = inorder[:mid]
            inorderRight = inorder[mid+1:]

            preorderLeft = preorder[1:mid+1]
            preorderRight = preorder[mid+1:]

            currentNode.left = df(preorderLeft, inorderLeft)
            currentNode.right = df(preorderRight, inorderRight)

            return currentNode

        return df(preorder, inorder)
    



        