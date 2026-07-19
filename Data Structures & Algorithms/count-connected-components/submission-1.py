class UF:
    def __init__(self, n):
        self.n = n
        self.parent = {i:i for i in range(n)}
        self.rank = n * [0]
    
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
            return
        if self.rank[u] < self.rank[v]:
            self.parent[v] = u
            self.rank[v] += 1
        elif self.rank[u] > self.rank[v]:
            self.parent[u] = v
            self.rank[u] += 1
        else:
            self.parent[v] = u
            self.rank[v] += 1
        self.n -= 1  

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n <= 1:
            return n
        uf = UF(n)
        for e in edges:
            uf.merge(e[0], e[1])
        return uf.n

        