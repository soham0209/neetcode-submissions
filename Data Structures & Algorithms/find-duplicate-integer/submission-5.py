class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
            else:
                return abs(num)
        