# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m = 0
        def dfs(cur):
            nonlocal m

            if not cur:
                return 0
            l = dfs(cur.left)
            r = dfs(cur.right)
            m = max(m, l + r)
            return 1 + max(l, r)
        
        dfs(root)
        return m