# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        positioner = head
        curr = head
        prev = None

        count = 0
        while positioner:
            if count >= n:
                prev = curr
                curr = curr.next

            positioner = positioner.next
            count += 1
        
        if curr == head:
            if head.next:
                head = head.next
            else:
                head = None
            return head
        
        print(prev.val)
        print(curr.val)

        prev.next = curr.next
        curr = None
        return head