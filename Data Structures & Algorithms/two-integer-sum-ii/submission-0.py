class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers) - 1
        for i, n in enumerate(numbers):
            k = target - n
            while numbers[j] > k:
                j -= 1
            if numbers[j] == k:
                return [i+1, j+1]
        