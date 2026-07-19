class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        does_exist = {}
        for i, n in enumerate(nums):
            key = target - n
            if key in does_exist:
                return [does_exist[key], i]
            does_exist[n] = i

        