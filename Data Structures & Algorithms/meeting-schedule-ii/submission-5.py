"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        active = {}
        for i in intervals:
            active[i.start] = 1 + active.get(i.start, 0)
            active[i.end] = active.get(i.end, 0) - 1
        res, count = 0, 0
        for t in sorted(active.keys()):
            count += active[t]
            res = max(count, res)
        return res
        