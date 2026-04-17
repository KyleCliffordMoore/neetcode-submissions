class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        area = 0
        maxArea = 0

        def inBounds(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[i])

        def bfs(start_i, start_j):
            nonlocal visited
            nonlocal area
            neighbors = deque([ (start_i, start_j) ])

            while neighbors:
                neighbor = neighbors.popleft()

                if neighbor in visited:
                    continue
                visited.add(neighbor)

                (i, j) = neighbor
                if grid[i][j] == 0:
                    continue
                
                # area code
                area += 1
                # print(f"Point: ({i}, {j}) w/ area = {area}")

                for (ioff, joff) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if inBounds(i + ioff, j + joff):
                        neighbors.append( (i + ioff, j + joff) )

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if (i, j) in visited:
                    continue
                
                if grid[i][j] == 0:
                    visited.add((i, j))
                    continue
                
                area = 0
                # print(f"Starting bfs... at ({i}, {j})")
                bfs(i, j)
                # print(f"Finished bfs ({i}, {j})")
                maxArea = max(maxArea, area)

        return maxArea