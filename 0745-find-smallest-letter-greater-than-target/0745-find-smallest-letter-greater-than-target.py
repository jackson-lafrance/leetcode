class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[len(letters)-1]:
            return letters[0]

        mem = ''
        left = 0
        right = len(letters)-1
        while left <= right:
            mid = (left+right)//2
            if letters[mid] > target:
                right = mid - 1
                mem = letters[mid]
            else:
                left = mid + 1
        return mem