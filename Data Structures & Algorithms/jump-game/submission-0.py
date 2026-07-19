class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = [False] * len(nums)
        reachable[0] = True
        for i, n in enumerate(nums):
            if not reachable[i]:
                continue
            curr = i
            while curr < len(nums) and curr <= (i + n):
                reachable[curr] = True
                curr += 1
        return reachable[-1]


            
        