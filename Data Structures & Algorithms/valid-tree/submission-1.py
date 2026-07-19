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
            return True
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
        return False
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n-1):
            return False
        uf = UF(n)
        for e in edges:
            has_cycle = uf.merge(e[0], e[1])
            if has_cycle:
                return False
        return uf.n == 1


        
        