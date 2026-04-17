class Solution:
    def isPathCrossing(self, path: str) -> bool:
        locs = set()

        currLocation = (0, 0) 
        locs.add(currLocation)

        for dir in path:
            offSet = [0, 0]
            if dir == "N":
                offSet[1] = 1
            elif dir == "S":
                offSet[1] = -1
            elif dir == "E":
                offSet[0] = 1
            else:
                offSet[0] = -1
            
            currLocation = (currLocation[0] + offSet[0], currLocation[1] + offSet[1])
            if currLocation in locs:
                return True
            locs.add(currLocation)
        
        return False
