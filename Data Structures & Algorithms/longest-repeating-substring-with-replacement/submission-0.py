class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans = 0
        l = 0
        for r, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r- l + 1)
        return ans

            

        