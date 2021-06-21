# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        #         curr1, curr2, prev = head, head, ListNode()
        #         if head and head.next: head = head.next

        #         while curr1 and curr1.next:
        #             prev.next=curr1.next
        #             curr2 = curr1.next
        #             curr1.next = curr2.next
        #             curr2.next = curr1

        #             prev = curr1
        #             curr1 = curr1.next
        #         return head
        """
        recursion
        """
        if not head or not head.next:
            return head
        temp = head
        head = head.next

        temp.next = head.next
        head.next = temp

        temp.next = self.swapPairs(temp.next)

        return head
