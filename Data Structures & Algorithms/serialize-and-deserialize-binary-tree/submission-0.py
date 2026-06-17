# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def df(root):
            if not root:
                res.append('N')
                return 
            res.append(str(root.val))
            df(root.left)
            df(root.right)
        df(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        vals = data.split(',')
        def df():
            if vals[self.i] == "N":
                self.i += 1
                return None
            root = TreeNode(int(vals[self.i]))
            self.i += 1
            root.left = df()
            root.right = df()
            return root
        return df()

        
