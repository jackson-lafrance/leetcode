class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        big = word2 if len(word2) > len(word1) else word1
        result = ''
        for i in range(len(big)):
            result += word1[i] if len(word1) > i else ''
            result += word2[i] if len(word2) > i else ''
        return result