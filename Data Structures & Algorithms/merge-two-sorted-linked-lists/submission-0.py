# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        a = list1
        b = list2

        result = ListNode()
        curr = result

        while a and b:
            if a.val < b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            curr = curr.next

        while a:
            curr.next = a
            a = a.next
            curr = curr.next
        
        while b:
            curr.next = b
            b = b.next
            curr = curr.next

        return result.next
                

