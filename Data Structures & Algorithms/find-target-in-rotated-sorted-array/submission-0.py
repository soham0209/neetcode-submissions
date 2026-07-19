class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        r = len(nums) + l - 1
        while l <= r:
            mid = l + (r - l) // 2
            mid_actual = mid % len(nums)
            if nums[mid_actual] == target:
                return mid_actual
            elif nums[mid_actual] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1 
        