class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        start = 0
        total_diff = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            total_diff += diff # To check if feasible
            if total < 0:
                total = 0
                start = i + 1 
        return start if total_diff >=0 else -1

        