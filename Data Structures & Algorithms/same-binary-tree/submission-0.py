# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.check(p, q)
    
    def check(self, t1, t2):
        if not t1:
            return not t2
        elif not t2:
            return False
        else:
            left, right = self.check(t1.left, t2.left), self.check(t1.right, t2.right)
            return left and right and t1.val == t2.val