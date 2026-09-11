# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        cur.val = -1001
        while cur:
            cur = cur.next
            if cur != None and cur.val == -1001:
                return True
            elif cur == None:
                break
            cur.val = -1001
        return False