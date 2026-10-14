# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(cur):
            if not cur:
                return "N"
            
            s = str(cur.val) + ","
            s += preorder(cur.left) + ","
            s += preorder(cur.right)
            return s
        
        return preorder(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        print(nodes)
        idx = 0
        def preorder():
            nonlocal idx
            if nodes[idx] == "N":
                idx += 1
                return None
            root = TreeNode(int(nodes[idx]))
            idx += 1
            root.left = preorder()
            root.right = preorder()
            return root
        return preorder()
