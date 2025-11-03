class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0
        direction = 0 

        for move in instructions:
            if move == 'G':
                x += dirs[direction][0]
                y += dirs[direction][1]
            elif move == 'L':
                direction = (direction + 3) % 4
            else:
                direction = (direction + 1) % 4

        return (x == 0 and y == 0) or direction != 0