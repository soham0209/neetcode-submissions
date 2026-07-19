class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, value):
            if i == len(nums) and value == target:
                return 1
            if i == len(nums) and value != target:
                return 0
            if (i, value) in dp:
                return dp[(i, value)]
            dp[(i, value)] = dfs(i+1, value+nums[i]) + dfs(i+1, value-nums[i])
            return dp[(i, value)]
        return dfs(0, 0)