class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort(key=lambda coordinate:coordinate[0])
        
        if (coordinates[1][0]-coordinates[0][0]) == 0:
            slope = None
        else:
            slope = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])

        for i in range(len(coordinates[:-1])):
            if slope == None:
                if coordinates[i+1][0]-coordinates[i][0] != 0:
                    return False
            else:
                if coordinates[i+1][0]-coordinates[i][0] == 0:
                    return False

                if (coordinates[i+1][1]-coordinates[i][1])/(coordinates[i+1][0]-coordinates[i][0]) != slope:
                    return False
        
        return True