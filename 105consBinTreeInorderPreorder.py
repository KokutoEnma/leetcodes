# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        inorder_index = {inorder[i]: i for i in range(len(inorder))}

        def build(start, end):
            nonlocal pre_index

            if start > end:
                return None

            curr_val = preorder[pre_index]
            curr = TreeNode(val=curr_val)

            pre_index += 1
            curr.left = build(start, inorder_index[curr_val]-1)
            curr.right = build(inorder_index[curr_val]+1, end)

            return curr

        pre_index = 0

        return build(0, len(inorder)-1)
