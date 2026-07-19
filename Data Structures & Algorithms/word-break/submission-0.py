class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = (len(s) + 1) * [float('inf')]
        dp[0] = 0
        def check_match(w, idx):
            i = 0
            if idx + len(w) > len(s):
                return float('inf')
            while i < len(w) and idx < len(s):
                if w[i] != s[idx]:
                    return float('inf')
                i += 1
                idx += 1
            return 1
        for j in range(len(s)+1):
            for w in wordDict:
                if j - len(w) >= 0:
                    dp[j] = min(dp[j], check_match(w, j-len(w))+ dp[j-len(w)])
        return True if dp[len(s)] < float('inf') else False
        