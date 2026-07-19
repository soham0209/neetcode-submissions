class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, t in enumerate(intervals):
            if newInterval[1] < t[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif t[1] < newInterval[0]:
                res.append(t)
            else:
                newInterval = [min(t[0], newInterval[0]), max(t[1], newInterval[1])]
        res.append(newInterval)
        return res
            





        
        