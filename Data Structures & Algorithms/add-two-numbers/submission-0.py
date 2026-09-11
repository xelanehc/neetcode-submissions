# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = 0
        power = 0
        while l1:
            s1 += l1.val * math.pow(10, power)
            power += 1
            l1 = l1.next
        
        s2 = 0
        power = 0
        while l2:
            s2 += l2.val * math.pow(10, power)
            power += 1
            l2 = l2.next
        
        s = (int)(s1 + s2)
        print(s)
        ret = ListNode(s % 10, None)
        prev = ret
        s = (int)(s / 10)

        while s != 0:
            v = s % 10
            add = ListNode(v)
            prev.next = add
            prev = add
            s = (int)(s / 10)

        return ret
