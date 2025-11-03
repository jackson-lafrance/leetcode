class Solution:
    def average(self, salary: List[int]) -> float:
        mini = 0
        maxi = 0
        total = 0
        for i in salary:
            if mini == 0:
                mini = i
                maxi = i
            if mini > i:
                mini = i
            if maxi < i:
                maxi = i
            total += i
        total -= mini
        total -= maxi

        return total / (len(salary)-2)