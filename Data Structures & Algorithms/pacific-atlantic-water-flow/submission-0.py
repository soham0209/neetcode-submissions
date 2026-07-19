class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 0:
            return [[]]
        ROWS, COLS = len(heights), len(heights[0])
        def bfs(src):
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            q = src
            ocean = set()
            while q:
                x, y = q.pop(0)
                ocean.add((x, y))
                for d in dirs:
                    x1, y1 = x + d[0], y + d[1]
                    if 0 <= x1 < ROWS and 0 <= y1 < COLS and (x1, y1) not in ocean and heights[x1][y1] >= heights[x][y]:
                        q.append((x1, y1))
            return ocean
        pac, atl = [], [] 
        for c in range(COLS):
            pac.append((0, c))
            atl.append((ROWS-1, c))
        for r in range(ROWS):
            pac.append((r, 0))
            atl.append((r, COLS-1))
        atl_visit = bfs(atl)
        pac_visit = bfs(pac)
        res = []
        for px, py in pac_visit:
            if (px, py) in atl_visit:
                res.append([px, py])
        return res



        
        