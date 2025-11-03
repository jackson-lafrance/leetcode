class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        counter1 = 10**len(num1)//10
        number1 = 0

        dicter = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

        for i in num1:
            number1 += dicter[i] * counter1
            counter1 = counter1 // 10

        counter2 = 10**len(num2)//10
        number2 = 0
        for i in num2:
            number2 += dicter[i] * counter2
            counter2 = counter2 // 10

        return str(number1 * number2)
        