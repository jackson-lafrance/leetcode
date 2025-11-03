class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle) - 1
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if length == j:
                    return i            
                        
        return -1

        