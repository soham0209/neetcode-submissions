
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def t(x, k):
            return math.ceil(x / k)
    
        def time_taken(piles, k):
            p = list(map(lambda x: t(x, k), piles))
            return sum(p)

        l = 1
        r = max(piles)
        res = l
        while l <= r:
            k = l + (r - l) // 2
            h_req = time_taken(piles, k)
            if h_req <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
            res = l
        return res

        