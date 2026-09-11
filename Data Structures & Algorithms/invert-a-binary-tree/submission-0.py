# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invertTreeHelper(root)
    
    def invertTreeHelper(self, cur) -> Optional[TreeNode]:
        if cur == None:
            return
        cur.left = self.invertTreeHelper(cur.left)
        cur.right = self.invertTreeHelper(cur.right)
        temp = cur.left
        cur.left = cur.right
        cur.right = temp
        return cur