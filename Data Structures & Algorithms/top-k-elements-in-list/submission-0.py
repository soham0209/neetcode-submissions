from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        freq_table = sorted([(k, v) for k, v in freq.items()], key=lambda x: x[1], reverse=True)
        res = [freq_table[i][0] for i in range(k)]
        return res

        