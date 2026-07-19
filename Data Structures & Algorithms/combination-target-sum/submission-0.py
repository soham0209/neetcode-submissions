class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subsets = []
        def dfs(i, target):
            if i < len(nums) and target == 0:
                res.append(subsets.copy())
                return
            if i >= len(nums) or target < 0:
                return
            subsets.append(nums[i])
            dfs(i, target-nums[i])
            subsets.pop()
            dfs(i+1, target)
        dfs(0, target)
        return res

        