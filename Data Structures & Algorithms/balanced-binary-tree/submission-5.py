# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(cur):
            nonlocal res

            if not cur:
                return 0
            
            l, r = dfs(cur.left), dfs(cur.right)
            if abs(l - r) > 1:
                res = False

            return 1 + max(l, r)
        
        dfs(root)
        return res