class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def lis(i, j):
            if i == len(nums):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if j == -1 or (j >= 0 and nums[i] > nums[j]):
                incl = 1 + lis(i+1, i)
            else:
                incl = 0
            excl = lis(i+1, j)
            dp[(i, j)] = max(incl, excl)
            return dp[(i, j)]
        return lis(0, -1)
        