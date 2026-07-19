class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)}
        for (ui, vi, ti) in times:
            adj[ui].append((vi, ti))
        shortest = {}
        minHeap = [(0, k)]
        maxTime = 0
        while minHeap:
            w, u = heapq.heappop(minHeap)
            if u in shortest:
                continue
            shortest[u] = w
            maxTime = max(maxTime, w)
            for (nbr, d) in adj[u]:
                heapq.heappush(minHeap, (w+d, nbr))
        
        for i in range(1, n+1):
            if i not in shortest:
                return -1
        return maxTime

        
        
        