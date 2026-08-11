# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # Reverse second half
        prev = None
        second = slow.next

        slow.next = None # IMPORTANT DISCONNECT THE TWO


        while second:
            next = second.next

            second.next = prev
            prev = second
            second = next
        
        # Merge lists
        first, second = head, prev

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
        