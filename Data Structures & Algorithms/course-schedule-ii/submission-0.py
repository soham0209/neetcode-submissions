class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for i in range(len(prerequisites)):
            b, a = prerequisites[i][1], prerequisites[i][0]
            adjlist[b].append(a)
            indegree[a] += 1
        q = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        res = []
        visited = 0
        while q:
            node = q.pop(0)
            visited += 1
            res.append(node)
            for neighbor in adjlist[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        if visited == numCourses:
            return res
        return []