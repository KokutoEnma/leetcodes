import math

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    
        
        """bucket"""
        bucket = {}
        w = t+1
        
        for i in range(len(nums)):
            id = math.floor(nums[i]/w)
            if id in bucket:
                return True
            if id+1 in bucket and w > abs(bucket[id+1] - nums[i]):
                return True
            if id-1 in bucket and w > abs(bucket[id-1] - nums[i]):
                return True
            bucket[id] = nums[i]
            if i >= k:
                del bucket[math.floor(nums[i-k]/w)]
        
        return False