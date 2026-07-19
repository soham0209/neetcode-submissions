class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i, n in enumerate(nums):
            res += i - n
        return len(nums) + res
        