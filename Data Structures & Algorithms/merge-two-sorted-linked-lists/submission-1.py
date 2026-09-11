# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        c1, c2 = list1, list2
        if not c1 and not c2:
            return
        elif not c1:
            return c2
        elif not c2:
            return c1

        cur = None
        if c1.val < c2.val:
            cur = c1
            c1 = c1.next
        else:
            cur = c2
            c2 = c2.next
        
        head = cur
        
        while c1 and c2:
            if c1.val < c2.val:
                cur.next = c1
                cur = cur.next
                c1 = c1.next
            else:
                cur.next = c2
                cur = cur.next
                c2 = c2.next
        
        while c1:
            cur.next = c1
            c1 = c1.next
            cur = cur.next
        
        while c2:
            cur.next = c2
            c2 = c2.next
            cur = cur.next

        return head