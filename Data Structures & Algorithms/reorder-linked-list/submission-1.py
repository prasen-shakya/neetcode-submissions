# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []

        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        res = []
        l = 0
        r = len(arr) - 1

        while l < r:
            res.append(arr[l])
            res.append(arr[r])
            l += 1
            r -= 1
        if l == r:
            res.append(arr[l])
        for val in res:
            head.val = val
            head = head.next