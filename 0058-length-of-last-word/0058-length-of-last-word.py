class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        v = s.strip().split(' ')
        return len(v[-1])