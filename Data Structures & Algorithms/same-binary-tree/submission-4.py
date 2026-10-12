# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p_node, q_node):
            if not p_node and not q_node:
                return True
            elif not p_node or not q_node:
                return False
            
            return p_node.val == q_node.val and dfs(p_node.left, q_node.left) and dfs(p_node.right, q_node.right)
        
        return dfs(p, q)