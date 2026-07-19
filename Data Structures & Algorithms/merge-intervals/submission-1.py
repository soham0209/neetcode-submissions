class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if not intervals:
            return res
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for t in intervals:
            if t[0] > res[-1][1]:
                res.append(t)
            else:
                res[-1][0] = min(res[-1][0], t[0])
                res[-1][1] = max(res[-1][1], t[1])
        return res


        
        