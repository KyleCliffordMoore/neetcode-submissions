class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        num_islands = 0

        def inBounds(i, j):
            if i < 0 or j < 0:
                return False
            if i >= len(grid) or j >= len(grid[i]):
                return False
            return True

        def bfs(start_i, start_j):
            nonlocal visited
            neighbors = deque([ (start_i, start_j) ])

            while neighbors:

                neighbor = neighbors.popleft()
                if neighbor in visited:
                    continue
                visited.add(neighbor)

                (i, j) = neighbor
                if grid[i][j] == "0":
                    # print("did this ever happen?")
                    continue

                for (ioff, joff) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if inBounds(i + ioff, j + joff):
                        neighbors.append( (i + ioff, j + joff) )

                # add all its neighbors to the queue     


        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if (i, j) in visited:
                    continue
                
                if grid[i][j] == "0":
                    visited.add((i, j))
                    continue

                print(f"Got here ({i}, {j})")
                # do bfs
                print(visited)
                bfs(i, j)
                print(visited, len(visited))
                #increase count
                num_islands += 1

        return num_islands