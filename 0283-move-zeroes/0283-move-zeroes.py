class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        position = 0

        for i in nums:
            if i != 0:
                nums[position] = i
                position += 1
            
        while position < len(nums):
            nums[position] = 0
            position += 1