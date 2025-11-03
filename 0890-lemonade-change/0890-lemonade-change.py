class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        total = 0
        five = 0
        ten = 0
        for i in bills:
            if i == 5:
                five += 1
            if i == 10:
                if five <= 0:
                    return False
                else:
                    ten += 1
                    five -= 1
            if i == 20:
                if ten <= 0:
                    if five < 3:
                        return False
                    else:
                        five -= 3
                else:
                    if five <= 0:
                        return False
                    else:
                        five -= 1
                        ten -= 1
        return True            
        