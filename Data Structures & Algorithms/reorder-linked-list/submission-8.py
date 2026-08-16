# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Identify middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split two halves
        cur = slow.next
        slow.next = None

        # Reverse second half
        prev = None 

        while cur:
            next = cur.next

            cur.next = prev
            prev = cur
            cur = next

        # Weave the two arrays
        cur1 = head
        cur2 = prev

        while cur1 and cur2:
            tmp1, tmp2 = cur1.next, cur2.next

            cur1.next = cur2
            cur2.next = tmp1

            cur1 = tmp1
            cur2 = tmp2
