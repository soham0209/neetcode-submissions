class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        l = 0
        res = []
        for r in range(len(nums)):
            heapq.heappush(pq, (-nums[r], r))
            if r >= k - 1:
                while pq and pq[0][1] < l:
                    heapq.heappop(pq)
                curr_max = -pq[0][0]
                res.append(curr_max)
                l += 1
        return res

        