class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for j in range(1, len(nums)):
            i = len(nums) - 1 - j
            output[i] = output[i+1] * nums[i+1]

        for j in range(len(nums)):
            output[j] = output[j] * prefix[j]
        return output
        



        