# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        pos = length - n
        cur = head
        if pos == 0:
            return head.next
        for i in range(pos - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head