class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        count = [v for v in count.values()]
        count.sort()
        maxf = count[-1]
        idle = (maxf - 1) * n
        for i in range(len(count)-2, -1, -1):
            idle = idle - min(maxf-1, count[i])
        return max(idle, 0) + len(tasks) 



        