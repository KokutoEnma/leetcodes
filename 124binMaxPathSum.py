# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ret = -float('inf')

        def trace(curr):
            nonlocal ret

            left = -float('inf') if not curr.left else trace(curr.left)
            right = -float('inf') if not curr.right else trace(curr.right)

            if left < 0 and right < 0:
                ret = max(ret, curr.val)
                return curr.val

            elif left < 0:
                ret = max(ret, curr.val+right)
                return curr.val+right

            elif right < 0:
                ret = max(ret, curr.val+left)
                return curr.val+left

            else:
                ret = max(ret, curr.val+left+right)
                return max(curr.val+left, curr.val+right)

        trace(root)

        return ret
