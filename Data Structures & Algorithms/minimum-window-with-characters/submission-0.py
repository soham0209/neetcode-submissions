class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "":
            return ""
        countT, countS = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        need, have = len(countT), 0
        l = 0
        res = [-1, -1]
        resLen = float("inf")
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            if s[r] in countT and countT[s[r]] == countS[s[r]]:
                have += 1
            while need == have:
                if r-l+1 < resLen:
                    res = [l, r]
                    resLen = min(resLen, r-l+1)
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
 
        