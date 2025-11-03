class Solution:
    def isPalindrome(self, x: int) -> bool:
        word = str(x)
        for i in range(len(word)):
            if word[i] != word[len(word)-1-i]:
                return False
        return True