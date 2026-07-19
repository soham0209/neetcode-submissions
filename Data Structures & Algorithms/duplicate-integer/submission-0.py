class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_dict = {}
        for i, n in enumerate(nums):
            if n in freq_dict:
                return True
            freq_dict[n] = i
        return False
         