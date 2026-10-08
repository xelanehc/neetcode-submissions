# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        fast, slow = head.next, head
        while fast and slow:
            if fast == slow:
                return True
            fast = fast.next.next if fast.next else None
            slow = slow.next
        
        return False