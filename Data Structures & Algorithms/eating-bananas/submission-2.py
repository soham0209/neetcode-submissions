class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(piles, h,  rate):
            s = 0
            for p in piles:
                s += math.ceil(p / rate)
            return s <= h

        l, r = 1, max(piles)
        while l < r:
            mid = l + (r - l) // 2
            if can_eat(piles, h, mid):
                r = mid
            else:
                l = mid + 1
        return l
        