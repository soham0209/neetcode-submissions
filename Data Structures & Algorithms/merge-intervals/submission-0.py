class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if not intervals:
            return res
        intervals = sorted(intervals, key=lambda x: x[0])
        output = [intervals[0]]
        for start, end in intervals:
            lastend = output[-1][1]
            if start <= lastend:
                output[-1][1] = max(end, lastend)
            else:
                output.append([start, end])
        return output


        
        