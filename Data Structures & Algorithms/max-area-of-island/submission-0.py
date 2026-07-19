class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(i, j, grid, visited):
            rows, cols = len(grid), len(grid[0])
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            islands = 0
            q = [(i, j)]
            while q:
                x, y = q.pop(0)
                if (x, y) in visited:
                    continue
                islands += 1
                visited.add((x, y))
                for d in dirs:
                    x1, y1 = x + d[0], y + d[1]
                    if x1 < 0 or x1 >= rows or y1 < 0 or y1 >= cols or (x1, y1) in visited or grid[x1][y1] == 0:
                        continue
                    q.insert(0, (x1, y1))
            return islands, visited 


        if len(grid) == 0:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    islands, visited = bfs(i, j, grid, visited)
                    res = max(res, islands)
        return res
                    
        