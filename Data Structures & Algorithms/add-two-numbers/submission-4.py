# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        dummy = ListNode(0, None)
        prev = dummy
        carry = 0

        while c1 and c2:
            total = c1.val + c2.val + carry
            num = total % 10
            carry = total // 10
            newNode = ListNode(num, None)
            prev.next = newNode
            prev = prev.next
            c1 = c1.next
            c2 = c2.next

        while c1:
            total = c1.val + carry
            num = total % 10
            carry = total // 10
            newNode = ListNode(num, None)
            prev.next = newNode
            prev = prev.next
            c1 = c1.next
        
        while c2:
            total = c2.val + carry
            num = total % 10
            carry = total // 10
            newNode = ListNode(num, None)
            prev.next = newNode
            prev = prev.next
            c2 = c2.next
        
        if carry:
            newNode = ListNode(carry, None)
            prev.next = newNode
        
        return dummy.next