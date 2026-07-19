class Solution:
    def mul_and_pad(self, d, num1, zeroes):
        s = 0
        c = 0
        res = ''
        for n in range(len(num1)-1, -1, -1):
            ans = int(num1[n]) * d
            s = (ans + c) % 10
            c = (ans + c) // 10
            res = str(s) + res
        if c > 0:
            res = str(c) + res
        for i in range(zeroes):
            res = res + '0'
        return res
    
    def add(self, s1, s2):
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        s, c = 0, 0
        res = ''
        i = len(s1) - 1
        for j in range(len(s2)-1, -1 , -1):
            s = (int(s1[i]) + int(s2[j]) + c) % 10
            c = (int(s1[i]) + int(s2[j]) + c) // 10
            res = str(s) + res
            i = i - 1
        for j in range(i, -1, -1):
            s = (int(s1[j]) + c) % 10
            c = (int(s1[j]) + c) // 10
            res = str(s) + res
        if c > 0:
            res = str(c) + res
        return res
        
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        res = ''
        pad_zeroes = 0
        for i in range(len(num2)-1, -1, -1):
            d = int(num2[i])
            tmp = self.mul_and_pad(d, num1, pad_zeroes)
            res = self.add(tmp, res)
            pad_zeroes = pad_zeroes + 1
        return res




        