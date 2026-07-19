class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curr_sum = 0
        for i in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            ans = max(curr_sum, ans)
        return ans
             

        