class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res = nums[0]
        for n in nums:
            tmp = currMax * n
            currMax = max(n, n*currMin, currMax*n)
            currMin = min(n, tmp, currMin*n)
            res = max(res, currMax)
        return res
        
        