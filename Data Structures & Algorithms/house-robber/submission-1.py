class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n < 3:
            return max(nums)
        b = nums[0]
        a = max(nums[0], nums[1])
        for i in range(2, n):
            tmp = a
            a = max(a, b + nums[i])
            b = tmp
        return a

        