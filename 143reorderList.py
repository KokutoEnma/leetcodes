# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.

        1. split the list into 2 halves
        2. reverse the second half
        3. merge them
        """

        # step 1 split the list into 2 halves
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 2. reverse the second half
        fast = slow.next
        slow.next = None

        prev = None
        while fast:
            tmp = fast.next
            fast.next = prev
            prev = fast
            fast = tmp

        # 3. merge them
        while head and prev:
            tmp1, tmp2 = head.next, prev.next
            head.next = prev
            prev.next = tmp1
            head = tmp1
            prev = tmp2
