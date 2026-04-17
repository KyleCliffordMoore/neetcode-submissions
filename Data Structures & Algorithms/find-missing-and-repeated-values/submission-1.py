class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        base = set( [i + 1 for i in range(len(grid) * len(grid[0]))] )
        mySet = set()
        duplicate = None

        for row in grid:
            for val in row:
                if val in mySet:
                    duplicate = val
                mySet.add(val)
        
        for missing in (base - mySet):
            return [duplicate, missing]