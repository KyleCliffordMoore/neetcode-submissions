class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        queue = deque([])
        visited = set()
        largest = -1

        numFresh = 0
        def findRottenOranges():
            nonlocal numFresh
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == ROTTEN:
                        queue.append( (i, j, 0) )
                    if grid[i][j] == FRESH:
                        numFresh += 1

        def inBounds(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[i])

        def bfs():
            nonlocal largest
            nonlocal numFresh
            while queue:
                (i, j, depth) = queue.popleft()

                if (i, j) in visited:
                    continue
                visited.add( (i, j) )

                # Rotting logic
                if grid[i][j] == FRESH:
                    largest = max(largest, depth)
                    grid[i][j] = ROTTEN
                    numFresh -= 1
                
                # print("rotten")

                for (ioff, joff) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    inew = i + ioff
                    jnew = j + joff
                    
                    if inBounds(inew, jnew) and grid[inew][jnew] == FRESH:
                        # print(inew, jnew, FRESH)
                        # print('appending')
                        queue.append( (inew, jnew, depth + 1) )


        findRottenOranges()
        if numFresh == 0:
            return 0
        bfs()

        print(numFresh)
        return largest if numFresh == 0 else -1
