# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        previous = slow.next = None
        while second:
            tmp = second.next
            second.next = previous
            previous = second
            second = tmp
        
        first, second = head, previous
        while second:
            tmp_first, tmp_second = first.next, second.next
            first.next = second
            second.next = tmp_first
            first, second = tmp_first, tmp_second
        
