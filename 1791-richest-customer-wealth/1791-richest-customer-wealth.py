class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = ''
        for i in accounts:
            if maxi == '':
                maxi = sum(i)
            else:
                maxi = max(sum(i), maxi)
        return maxi
        