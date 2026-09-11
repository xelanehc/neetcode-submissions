# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next: # find halfway point
            slow = slow.next
            fast = fast.next.next
            
        cur = slow.next
        prev = slow.next = None
        while cur: # reverse
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        first, second = head, prev
        while second: #merge
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2