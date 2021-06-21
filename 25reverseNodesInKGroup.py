# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 1:
            return head

        start = end = curr = head
        size = 0

        while curr and size < k:
            end = curr
            size += 1
            curr = curr.next

        if size == k:
            size = 0
            curr2, prev = head, None
            while size < k and curr2:
                forward = curr2.next
                curr2.next = prev
                prev = curr2
                curr2 = forward
                size += 1

            head.next = self.reverseKGroup(curr, k)
            return end

        return head
