# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        m = 1
        while cur.next:
            cur = cur.next
            m += 1
        dummy = cur = ListNode()
        cur.next = head
        dummy.next = head
        for i in range(m - n):
            cur = cur.next
        if cur.next:
            if cur.next.next:
                cur.next = cur.next.next
            else:
                cur.next = None
        else:
            cur.next = None
        return dummy.next