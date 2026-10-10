# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        cur = head
        while cur:
            cur = cur.next
            l += 1
        
        stop = l - n
        if stop == 0:
            return head.next
        
        cur = head
        i = 1
        while cur and i < stop:
            cur = cur.next
            i += 1
        cur.next = cur.next.next

        return head