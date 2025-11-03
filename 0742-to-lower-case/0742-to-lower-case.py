class Solution:
    def toLowerCase(self, s: str) -> str:
        string = ''
        for i in s:
            if ord(i) <= 90 and ord(i) >= 65:
                string += chr(ord(i)+32)
            else:
                string += i
        return string