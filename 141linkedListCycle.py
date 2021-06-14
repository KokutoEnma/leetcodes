# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pos = ListNode(1234567)

        while head:
            if head.val == 1234567:
                return True
            prev = head
            head = head.next
            prev.next = pos

        return False
