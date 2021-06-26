class Solution:
    def trap(self, height: List[int]) -> int:
        """two pointers"""

        left, right = 0, len(height)-1
        left_max = right_max = 0
        ret = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ret += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ret += right_max-height[right]
                right -= 1
        return ret

        """stack"""
#         if len(height)<1: return 0

#         stack = []
#         ret = 0

#         for i in range(len(height)):
#             while stack and height[i]>height[stack[-1]]:
#                 top = stack.pop()
#                 if not stack: break
#                 w = i-stack[-1]-1
#                 h = min(height[i],height[stack[-1]]) - height[top]
#                 ret += w*h
#             stack.append(i)

#         return ret

        """dynamic programming"""
#         if len(height)<1: return 0

#         k=len(height)

#         dp_left = [0]*k
#         dp_right = [0]*k

#         dp_left[0] = height[0]
#         dp_right[-1] = height[-1]

#         for i in range(1, k):
#             dp_left[i] = max(height[i], dp_left[i-1])

#         for i in range(k-2, -1, -1):
#             dp_right[i] = max(height[i], dp_right[i+1])

#         print(dp_left)
#         print(dp_right)

#         ret = 0
#         for i in range(k):
#             ret += min(dp_right[i], dp_left[i]) - height[i]

#         return ret
