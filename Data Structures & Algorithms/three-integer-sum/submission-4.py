class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        nums = sorted(nums)
        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1         
        return res



        