# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path, q_path = [], []

        def dfs(cur, path):
            nonlocal p_path
            nonlocal q_path
            if not cur:
                return
            
            path.append(cur)
            if cur.val == p.val:
                p_path = path[:]
            if cur.val == q.val:
                q_path = path[:]
            
            dfs(cur.left, path)
            dfs(cur.right, path)

            path.pop()

        dfs(root, [])

        for i in range(len(p_path) - 1, -1, -1):
            for j in range(len(q_path) - 1, -1, -1):
                if p_path[i] == q_path[j]:
                    return p_path[i]

        return -1
