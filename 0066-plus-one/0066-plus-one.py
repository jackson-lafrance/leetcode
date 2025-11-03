class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        backNewDigits = []
        bonus = False
        backDigits = digits[::-1]

        first = backDigits[0] + 1
        if first >= 10:
            bonus = True
            backNewDigits.append((first) % 10)
            for i in backDigits[1:]:
                if bonus:
                    bonus = False
                    if i + 1 >= 10:
                        bonus = True
                        backNewDigits.append((i + 1) % 10)
                    else:
                        backNewDigits.append(i+1)
                else:
                    backNewDigits.append(i)
            if bonus:
                backNewDigits.append(1)
            return backNewDigits[::-1]
        else:
            digits[len(digits)-1] += 1
            return digits
                        
            