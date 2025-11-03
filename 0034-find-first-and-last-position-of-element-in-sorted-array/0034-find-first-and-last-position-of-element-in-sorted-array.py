class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        if target not in nums:
            return [-1, -1]
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                faker1 = faker2 = mid
                while faker1 > 0:
                    if nums[faker1-1] == target:
                        faker1 -= 1
                    else:
                        break
                while faker2 < len(nums)-1:
                    if nums[faker2 + 1] == target:
                        faker2 += 1
                    else: 
                        break
                return [faker1, faker2]