# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        cur = lists[0]
        for i in range(1, len(lists)):
            cur = self.mergeTwoLists(cur, lists[i])
        return cur
        
    def mergeTwoLists(self, list1, list2) -> Optional[ListNode]:
        dummy = cur = ListNode()
        
        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next
        
        cur.next = list1 or list2
        return dummy.next