# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(cur):
            if not cur:
                return -1
            if cur.val < p.val and cur.val < q.val:
                return dfs(cur.right)
            elif cur.val > p.val and cur.val > q.val:
                return dfs(cur.left)
            else:
                return cur
        
        return dfs(root)