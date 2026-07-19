class UF:
    def __init__(self, n):
        self.parent = {i:i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}
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
        if self.rank[u]<= self.rank[v]:
            self.parent[v] = u
            self.rank[v] += 1
        else:
            self.parent[u] = v
            self.rank[u] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                wt = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((i, j, wt))
        edges = sorted(edges, key=lambda x : x[2])
        uf = UF(n)
        res = 0
        count = 0
        for (u, v, wt) in edges:
            if uf.merge(u, v):
                count += 1
                res += wt
            if count == (n-1):
                return res
        return res


        