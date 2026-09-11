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
        def dfs(cur):
            if not cur:
                res.append("N")
                return
            res.append(str(cur.val))
            dfs(cur.left)
            dfs(cur.right)
        
        dfs(root)
        return ".".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(".")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            val = int(vals[self.i])
            cur = TreeNode(val)
            self.i += 1
            cur.left = dfs()
            cur.right = dfs()
            return cur
        
        return dfs()