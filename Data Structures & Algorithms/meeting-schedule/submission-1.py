"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)
        if len(intervals) <= 1:
            return True
        busy = intervals[0].end
        for x in intervals[1:]:
            if x.start < busy:
                return False
            busy = max(busy, x.end)
        return True
