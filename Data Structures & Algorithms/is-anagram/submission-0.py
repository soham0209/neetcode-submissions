class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_dict = {}
        for c in s:
            if c not in freq_dict:
                freq_dict[c] = 0
            freq_dict[c] += 1
        for c in t:
            if c not in freq_dict:
                return False
            freq_dict[c] -= 1
        for k, v in freq_dict.items():
            if v != 0:
                return False
        return True        