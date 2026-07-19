class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = defaultdict(int)
        for c in s1:
            s1_count[c] += 1
        l, r = 0, len(s1)-1
        s2_count = defaultdict(int)
        for i in range(len(s1)):
            s2_count[s2[i]] += 1

        def check_dicts(s1_count, s2_count):
            for k, v in s1_count.items():
                if k not in s2_count:
                    return False
                if v != s2_count[k]:
                    return False
            return True
        has_anagram = check_dicts(s1_count, s2_count)
        if has_anagram:
            return True
        while r < len(s2)-1:
            s2_count[s2[l]] -= 1
            l += 1
            r += 1
            s2_count[s2[r]] += 1
            has_anagram = check_dicts(s1_count, s2_count)
            if has_anagram:
                return True
        return False