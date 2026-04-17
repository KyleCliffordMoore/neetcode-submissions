class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        WATER = -1
        CHEST = 0
        LAND = 2147483647

        def inBounds(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[i])

        def bfs(myqueue):
            
            while myqueue:
                (i, j, depth) = myqueue.popleft()

                if grid[i][j] == WATER:
                    continue
        
                # our land logic
                if depth > grid[i][j]:
                    continue
                grid[i][j] = depth

                for (ioff, joff) in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:
                    if inBounds(i + ioff, j + joff):
                        myqueue.append( (i + ioff, j + joff, depth + 1) )



        myqueue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == CHEST:
                    myqueue.append( (i, j, 0) )
        
        bfs(myqueue)