# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = 0

        def dfs(cur):
            nonlocal cnt, res
            if not cur:
                return
            
            dfs(cur.left)
            if cnt == 0:
                return
            cnt -= 1
            if cnt == 0:
                res = cur.val
                return
            dfs(cur.right)
        
        dfs(root)
        return res