class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [['','',''],['','',''],['','','']]
        player = 'A'
        for i in moves:
            grid[i[0]][i[1]] = player
            if player == 'A':
                player = 'B' 
            else:
                player = 'A'

        for i in range(len(grid)):
            if grid[i][0] == grid[i][1] and grid[i][0] == grid[i][2] and grid[i][0] != '':
                return grid[i][0]       
            if grid[0][i] == grid[1][i] and grid[0][i] == grid[2][i] and grid[0][i] != '':
                return grid[0][i]

        if grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2] and grid[0][0] != '':
            return grid[0][0]
        
        if grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0] and grid[0][2] != '':
            return grid[0][2]

        if len(moves) == 9:
            return 'Draw'
        return 'Pending'