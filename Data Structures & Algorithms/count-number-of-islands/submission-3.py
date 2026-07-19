from typing import List
class UF:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i:0 for i in range(n)}

    
    def find(self, x):
        tmp = x
        while self.parent[tmp] != tmp:
            self.parent[tmp] = self.parent[self.parent[tmp]]
            tmp = self.parent[tmp]
        return tmp
    def merge(self, x, y):
        u = self.find(x)
        v = self.find(y)
        if u == v:
            return False
        if self.rank[u] >= self.rank[v]:
            self.parent[v] = u
            self.rank[u] += self.rank[v]
        else:
            self.parent[u] = v
            self.rank[v] += self.rank[u]
        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) < 1:
            return 0
        nrows = len(grid)
        ncols = len(grid[0])
        uf = UF(nrows * ncols)
        island = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == '0':
                    continue
                u = i * ncols + j
                island += 1
                for d in dirs:
                    ni, nj = i + d[0], j + d[1]
                    if ni < 0 or ni >= nrows or nj < 0 or nj >= ncols or grid[ni][nj] == '0':
                        continue
                    v = ni * ncols + nj
                    if uf.merge(u, v):
                      island -= 1
        return island
