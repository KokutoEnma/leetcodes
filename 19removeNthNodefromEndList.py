# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        curr1 = curr2 = head

        curr_size = 1
        while curr1.next:
            curr1 = curr1.next
            if curr_size > n:
                curr2 = curr2.next
            curr_size += 1

        # important corner case
        if curr_size == n:
            return head.next

        curr2.next = curr2.next.next
        return head
