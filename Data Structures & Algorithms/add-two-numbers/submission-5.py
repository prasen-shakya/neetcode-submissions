# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()

        carry = 0 

        while l1 or l2:
            total = 0

            if not l1:
                total = l2.val + carry
            elif not l2:
                total = l1.val + carry
            else:
                total = l1.val + l2.val + carry

            carry = total // 10
            tail.next = ListNode(total % 10)

            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry != 0:
            tail.next = ListNode(carry)
        
        return dummy.next


