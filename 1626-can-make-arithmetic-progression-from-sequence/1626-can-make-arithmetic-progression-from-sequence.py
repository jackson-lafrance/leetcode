class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        difference = 0
        for i in range(len(arr)):
            if i == 0:
                difference = arr[i+1] - arr[i]
            elif i < len(arr) - 1:
                if difference != arr[i+1] - arr[i]:
                    return False
        return True
        