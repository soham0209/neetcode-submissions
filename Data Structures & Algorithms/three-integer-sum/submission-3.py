class Solution:
    def twoSum(self, x, nums, target):
        res = []
        for i, n in enumerate(nums):
            k = target - n
            j = len(nums) - 1
            while i < j and nums[j] > k:
                j -= 1
            if nums[j] == k and i!=j:
                res.append([x, n, nums[j]])
        return res
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums = sorted(nums)
        ans = set()
        for i, n in enumerate(nums):
            target = 0 - n
            res = self.twoSum(n, nums[i+1:], target)
            if res:
                for l in res:
                    ans.add(tuple((sorted((l)))))
        return [list(x) for x in ans]


        