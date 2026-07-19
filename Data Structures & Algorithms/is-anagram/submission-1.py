class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
        for c in t:
            if c not in d:
                return False
            else:
                d[c] = d[c] - 1
            if c in d and d[c] < 0:
                return False
        for k, v in d.items():
            if v != 0:
                return False
        return True




        