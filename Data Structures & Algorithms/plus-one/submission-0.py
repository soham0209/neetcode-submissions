class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = len(digits) - 1
        s = (digits[r] + 1) % 10
        c = (digits[r] + 1) // 10
        digits[r] = s
        r -= 1
        while c > 0 and r >=0:
            s = (digits[r] + c) % 10
            c = (digits[r] + c) // 10
            digits[r] = s
            r -= 1
        if c == 1 and r == -1:
            digits.insert(0, 1)
        return digits
        