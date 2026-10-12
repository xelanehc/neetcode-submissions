# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True

        def checkSame(t1, t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            return t1.val == t2.val and checkSame(t1.left, t2.left) and checkSame(t1.right, t2.right)
        
        def dfs(cur):
            if not cur:
                return False
            
            if checkSame(cur, subRoot):
                return True
            return dfs(cur.left) or dfs(cur.right)
        
        return dfs(root)