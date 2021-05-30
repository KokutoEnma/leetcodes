class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        """
        recursion
        """
        

#         if len(nums)<3:
#             return min(nums)
#         mid_ind = int(len(nums)/2)
    
        
#         if nums[mid_ind]<nums[mid_ind-1] and nums[mid_ind]<nums[mid_ind+1]:
#             return nums[mid_ind]
        
        
#         return min(self.findMin(nums[:mid_ind]),self.findMin(nums[mid_ind+1:]))


        """
        iteration, left, right
        """

        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums)-1
        while left<=right:
            while nums[right] == nums[right-1] and left<=right:
                right-=1
            mid = (left+right)//2
            
            if nums[mid] < nums[mid - 1]:
                break
            
            elif nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        
        return nums[mid]
                
            
            