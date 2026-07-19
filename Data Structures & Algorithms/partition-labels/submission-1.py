class Solution:
    # Map this problem to merge interval
    # We don't need to sort the intervals since they 
    # are already sorted by construction
    def partitionLabels(self, s: str) -> List[int]:
        freqMap = {}
        intervals = []
        for i, c in enumerate(s):
            if c not in freqMap:
                freqMap[c] = len(intervals)
                intervals.append([i, i])
                
            else:
                idx = freqMap[c]
                intervals[idx][1] = i
        ans = [intervals[0]]
        for interval in intervals:
            if interval[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans.append(interval)
        ans = [t[1]-t[0]+1 for t in ans]
        return ans
                




        
        


        