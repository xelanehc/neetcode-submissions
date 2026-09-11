# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        ret = 0
        def inOrder(cur, k):
            nonlocal n, ret
            if not cur:
                return
            inOrder(cur.left, k)
            n += 1
            if n == k:
                ret = cur.val
            inOrder(cur.right, k)
        inOrder(root, k)
        return ret