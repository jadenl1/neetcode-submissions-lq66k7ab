# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = head
        back = head
        backPrev = None

        for i in range(n-1):
            front = front.next
        
        while front.next:
            front = front.next

            backPrev = back
            back = back.next

        # back is now the nth node from end of list
        if back == head:
            head = head.next
        else:
            backPrev.next = back.next

        return head

