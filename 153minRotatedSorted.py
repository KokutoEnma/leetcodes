class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        """iteration, left, right"""
        left = 0
        right = len(nums)-1
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = (left + right)//2
            if nums[left] > nums[mid]:
                right = mid
            else:
                left = mid + 1
        
        """recursion"""
        
#         if len(nums)<3:
#             return min(nums)
#         mid_ind = int(len(nums)/2)
    
        
#         if nums[mid_ind]<nums[mid_ind-1] and nums[mid_ind]<nums[mid_ind+1]:
#             return nums[mid_ind]
        
        
#         return min(self.findMin(nums[:mid_ind]),self.findMin(nums[mid_ind+1:]))