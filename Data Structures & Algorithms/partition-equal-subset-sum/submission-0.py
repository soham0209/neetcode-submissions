class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target_sum = sum(nums)
        if target_sum % 2 == 1:
            return False
        target_sum = target_sum // 2
        dp = {}
        def dfs(i, total):
            if i == len(nums):
                return True if total == target_sum else False
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = dfs(i+1, total) or dfs(i+1, total+nums[i])
            return dp[(i, total)]
        return dfs(0, 0)
        