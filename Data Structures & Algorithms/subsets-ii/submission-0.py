class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def dfs(i, res):
            if i >= len(nums):
                ans.append(res.copy())
                return
            res.append(nums[i])
            dfs(i+1, res)
            res.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            dfs(i+1, res)
        dfs(0, [])
        return ans
            
                

        