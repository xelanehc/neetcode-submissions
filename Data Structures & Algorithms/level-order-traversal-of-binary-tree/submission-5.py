# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        q = deque([root])
        res = []

        while q:
            level = []

            for i in range(len(q)):
                cur = q.popleft()
                level.append(cur.val)

                l = cur.left if cur.left else None
                r = cur.right if cur.right else None
                if l:
                    q.append(l)
                if r:
                    q.append(r)
            
            res.append(level)
        
        return res
