class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        ans = 0
        l = 0
        maxfreq = 0
        for r, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)
            maxfreq = max(maxfreq, count[c])
            while (r - l + 1) - maxfreq > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r- l + 1)
        return ans

            

        