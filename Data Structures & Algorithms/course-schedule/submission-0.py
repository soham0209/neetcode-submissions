class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj =[[] for _ in range(numCourses)]
        for e in prerequisites:
            adj[e[0]].append(e[1])
        visited = {}
        def dfs(u, adj, visited):
            children = adj[u]
            visited[u] = 1
            for c in children:
                if c in visited and visited[c] == 1:
                    return False
                if c in visited and visited[c] == 2:
                    continue
                dfs_stat = dfs(c, adj, visited)
                if not dfs_stat:
                    return False
            visited[u] = 2
            return True
        for i in range(numCourses):
            if i in visited and visited[i] == 2:
                continue
            status = dfs(i, adj, visited)
            if not status:
                return False
        return True
            
            



        