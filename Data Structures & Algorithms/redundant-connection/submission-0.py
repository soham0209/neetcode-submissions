class UF:
    def __init__(self, n):
        self.parent = {i:i for i in range(1, n+1)}
        self.rank = {i: 0 for i in range(1, n+1)}
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        pos_edges = []
        uf = UF(len(edges))
        for e in edges:
            if not uf.merge(e[0], e[1]):
                return e



        