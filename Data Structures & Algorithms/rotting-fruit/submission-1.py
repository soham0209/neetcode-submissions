class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return -1
        def bfs(q, grid):
            rows = len(grid)
            cols = len(grid[0])
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            mins = 0
            while q:
                x, y, h = q.pop(0)
                if grid[x][y] == 2:
                    continue
                grid[x][y] = 2
                mins = max(mins, h)
                for d in dirs:
                    x1, y1 = x + d[0], y + d[1]
                    if x1 < 0 or x1 >= rows or y1 < 0 or y1 >= cols or grid[x1][y1] ==0 or grid[x1][y1] == 2:
                        continue
                    q.append((x1, y1, h+1))
            return grid, mins
        
        q = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    grid[i][j] = -2
        grid, mins = bfs(q, grid)
        print(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return mins

        