class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs = sorted(pairs, key=lambda x: x[0], reverse=True)
        fleet = cur_time = 0
        for p, s in pairs:
            dest = (target - p) / s
            if cur_time < dest:
                fleet += 1
                cur_time = dest
        return fleet