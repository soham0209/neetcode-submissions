class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        pq = []
        for k, v in count.items():
            heapq.heappush(pq, -v)
        time = 0
        q = []
        while pq or q:
            time += 1
            if pq:
                cnt = 1 + heapq.heappop(pq)
                if cnt < 0:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                cnt, t = q.pop(0)
                heapq.heappush(pq, cnt)
        return time



        