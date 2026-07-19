class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        res = 1
        for n in nums_set:
            tmp = n
            count = 1
            while (tmp + 1) in nums_set:
                count += 1
                res = max(res, count)
                tmp = tmp + 1
        return res



        
        