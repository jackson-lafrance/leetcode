class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ''
        minStr = -1
        for i in strs:
            if minStr == -1:
                minStr = i
            if len(i) < len(minStr):
                minStr = i
        
        for i in strs:
            if minStr == '':
                return ''
            for j in range(len(minStr)):
                if minStr[j] == i[j]:
                    longest += i[j]
                else:
                    break
            minStr = longest
            longest = ''
        return minStr