# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Move n nodes
        fast = head

        while n != 0:
            fast = fast.next
            n -= 1
        
        dummy = slow = ListNode(0, head)

        while fast:
            slow = slow.next
            fast = fast.next
        
        next = slow.next

        slow.next = slow.next.next

        return dummy.next