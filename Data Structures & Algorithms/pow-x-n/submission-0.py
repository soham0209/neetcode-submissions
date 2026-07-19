class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recur(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            a = self.myPow(x, n//2)
            res = a * a
            if n % 2 == 0:
                return res
            else:
                return res * x
        if x == 0:
            return x
        if n < 0:
            x = 1./x
            n = -n
        return recur(x, n)
     
            

        