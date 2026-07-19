class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if len(grid) == 0:
            return 0
        
        def bfs(i, j, grid):
            visited = set()
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            q = [(i, j, 0)]
            rows = len(grid)
            cols = len(grid[0])
            while q:
                x, y, h = q.pop(0)
                grid[x][y] = min(h, grid[x][y])
                visited.add((x, y))
                for d in dirs:
                    x1, y1 = x + d[0], y + d[1]
                    if x1 < 0 or x1 >= rows or y1 < 0 or y1 >=cols or grid[x1][y1] <= 0 or (x1, y1) in visited:
                        continue
                    q.append((x1, y1, h+1))
            return grid
        
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    grid = bfs(i, j, grid)


        