class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        charset = set()
        ans = 0
        while r < len(s):
            if s[r] not in charset:
                charset.add(s[r])
                ans = max(ans, r-l+1)
                r+=1
            else:
                charset.remove(s[l])
                l+=1
        return ans
        