# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        curr = result

        a, b = l1, l2
        carry = 0

        while a or b:
            vA = a.val if a else 0
            vB = b.val if b else 0

            val = vA + vB + carry
            digit = val % 10
            carry = val // 10

            curr.next = ListNode(digit)

            curr = curr.next
            a = a.next if a else None    
            b = b.next if b else None

        if carry != 0:
            curr.next = ListNode(carry)
        
        
        return result.next