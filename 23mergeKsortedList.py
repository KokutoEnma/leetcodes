# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if len(lists) < 1:
            return None

        while len(lists) > 1:
            tmp = []
            for i in range(0, len(lists), 2):
                tmp.append(self.merge2(lists[i:i+2]))

            lists = tmp

        return lists[0]

    def merge2(self, lists):
        if len(lists) < 2:
            return lists[0]

        l1, l2 = lists
        ret = ListNode()
        curr = ret

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if not l1:
            curr.next = l2
        else:
            curr.next = l1

        return ret.next

# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         def merge2Lists(l1, l2):
#             curr = head = ListNode()
#             while l1 and l2:
#                 if l1.val<l2.val:
#                     curr.next = l1
#                     l1 = l1.next
#                 else:
#                     curr.next = l2
#                     l2 = l1
#                     l1 = curr.next.next
#                 curr = curr.next

#             if not l1:
#                 curr.next = l2
#             else:
#                 curr.next = l1
#             return head.next

#         amount = len(lists)
#         interval = 1
#         while interval < amount:
#             for i in range(0, amount - interval, interval * 2):
#                 lists[i] = merge2Lists(lists[i], lists[i + interval])
#             interval *= 2
#         return lists[0] if amount > 0 else None
