class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        topk = []
        for n in nums:
            heapq.heappush(topk, n)
            if len(topk) > k:
                heapq.heappop(topk)
        return topk[0]

        