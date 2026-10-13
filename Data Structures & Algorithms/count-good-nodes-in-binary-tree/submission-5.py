# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return []
        
        res = 0

        def dfs(cur, m):
            nonlocal res
            
            if not cur:
                return
            
            if cur.val >= m:
                res += 1
                m = cur.val

            dfs(cur.left, m)
            dfs(cur.right, m)
            

        dfs(root, root.val)
        return res