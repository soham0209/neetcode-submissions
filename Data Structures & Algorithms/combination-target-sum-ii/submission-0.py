class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            curr.append(candidates[i])
            dfs(i+1, curr, total+candidates[i])
            curr.pop()
            idx = i+1
            while idx < len(candidates) and candidates[idx] == candidates[idx-1]:
                idx += 1
            dfs(idx, curr, total)
        dfs(0, [], 0)
        return res
        
        