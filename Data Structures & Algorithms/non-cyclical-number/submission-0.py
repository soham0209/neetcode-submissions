class Solution:
    def isHappy(self, n: int) -> bool:
        num_seen = set()
        tmp = n
        while True:
            res = 0
            while tmp != 0:
                d = (tmp % 10)
                res += d * d
                tmp = tmp // 10
            if res == 1:
                return True
            tmp = res
            if tmp in num_seen:
                return False
            num_seen.add(tmp)
        return False


        