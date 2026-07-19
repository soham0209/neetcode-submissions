class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if len(grid) == 0:
            return 0
        
        def bfs(q, grid):
            INF = 2**31 - 1
            visited = set()
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            rows = len(grid)
            cols = len(grid[0])
            while q:
                x, y, h = q.pop(0)
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                grid[x][y] = h
                
                for d in dirs:
                    x1, y1 = x + d[0], y + d[1]
                    if x1 < 0 or x1 >= rows or y1 < 0 or y1 >=cols or grid[x1][y1]<=0 or (x1, y1) in visited:
                        continue
                    q.append((x1, y1, h+1))
            return grid
        
        rows = len(grid)
        cols = len(grid[0])
        q = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        grid = bfs(q, grid)
                    


        