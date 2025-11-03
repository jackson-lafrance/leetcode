class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        way = 'none'
        for i in range(len(nums)):
            if i < len(nums) - 1:
                if way == 'none':
                    if nums[i+1] - nums[i] > 0:
                        way = 'inc'
                    elif nums[i+1] - nums[i] < 0:
                        way = 'dec'
                elif way == 'inc':
                    if nums[i+1] - nums[i] < 0:
                        return False
                else:
                    if nums[i+1] - nums[i] > 0:
                        return False
        return True
                    
