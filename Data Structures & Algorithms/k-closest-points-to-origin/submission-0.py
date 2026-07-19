class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for p in points:
            d = p[0]*p[0] + p[1]*p[1]
            heapq.heappush(h, (-d, p[0], p[1]))
            if len(h) > k:
                heapq.heappop(h)
        ans = [(a, b) for d, a, b in h]
        return ans
        