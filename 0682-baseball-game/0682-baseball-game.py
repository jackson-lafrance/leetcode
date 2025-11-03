class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            if operations[i] == '+':
                record.append(record[-1]+record[-2])
            elif operations[i] == 'D':
                record.append(record[-1]*2)
            elif operations[i] == 'C':
                del record[-1]
            else:
                record.append(int(operations[i]))
        return sum(record)

    