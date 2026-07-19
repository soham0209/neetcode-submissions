class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, n):
            if n == target:
                res.append(cur.copy())
                return
            for j in range(i, len(nums)):
                if nums[j] + n > target:
                    continue
                cur.append(nums[j])
                dfs(j, cur, n+nums[j])
                cur.pop()
        dfs(0, [], 0)
        return res

        