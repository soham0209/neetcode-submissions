class Solution:
    def climbStairs(self, n: int) -> int:
        a = 2
        b = 1
        if n < 3:
            return n
        for i in range(3, n+1):
            tmp = a + b
            b = a
            a = tmp
            # print(f"a={a} b={b}")
        return tmp

        