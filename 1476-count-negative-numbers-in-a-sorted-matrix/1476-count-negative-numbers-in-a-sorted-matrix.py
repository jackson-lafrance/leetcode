class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        for i in grid:
            left = 0
            right = len(i) - 1
            mem = len(i)
            while left <= right:
                mid = (left + right) // 2
                if i[mid] < 0:
                    mem = mid
                    right = mid - 1
                else:
                    left = mid + 1
            total += len(i) - mem
        return total
