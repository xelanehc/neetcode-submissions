# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        prev = slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        forward, reverse = head, prev
        while reverse:
            temp1, temp2 = forward.next, reverse.next
            forward.next = reverse
            forward = temp1
            reverse.next = forward
            reverse = temp2