class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        
        nums.sort()
        
        ret = []
        for i in range(len(nums)):
            if nums[i]>0:
                break
            left, right, sum = i+1, len(nums)-1, 0-nums[i]
            
            if i == 0 or nums[i] != nums[i-1]:
                while left<right:
                    if nums[left]+nums[right] == sum:
                        ret.append([nums[i], nums[left], nums[right]])
                        while left<right and nums[left] == nums[left+1]:
                            left+=1
                        while left<right and nums[right] == nums[right-1]:
                            right-=1

                        left+=1
                        right-=1

                    elif nums[left]+nums[right] < sum:
                        left+=1
                    else:
                        right-=1
            

        return ret
