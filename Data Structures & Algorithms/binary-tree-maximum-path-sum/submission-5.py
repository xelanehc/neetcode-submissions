# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(cur):
            nonlocal res
            if not cur:
                return 0
            
            left = max(dfs(cur.left), 0)
            right = max(dfs(cur.right), 0)
            res = max(res, left + cur.val + right)
            
            return cur.val + max(left, right)
        
        dfs(root)
        return res