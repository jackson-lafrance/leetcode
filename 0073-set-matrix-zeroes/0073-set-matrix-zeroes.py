class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []

        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    zeros.append([i,j])
        
        for i in zeros:
            for j in range(r):
                matrix[j][i[1]] = 0
            for j in range(c):
                matrix[i[0]][j] = 0
            
            