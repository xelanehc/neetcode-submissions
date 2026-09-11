# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.findRoot(root, subRoot)

    def findRoot(self, cur, subRoot):
        if not subRoot:
            return True
        if not cur:
            return False
        left = self.findRoot(cur.left, subRoot)
        right = self.findRoot(cur.right, subRoot)
        if self.check(cur, subRoot):
            return True
        return left or right

    def check(self, t1, t2):
        if not t1:
            return not t2
        elif not t2:
            return False
        else:
            left, right = self.check(t1.left, t2.left), self.check(t1.right, t2.right)
            return left and right and t1.val == t2.val