class Solution:
    
    def numDecodings(self, s: str) -> int:
        encodings = set([str(i) for i in range(1, 27)])
        dp = [-1] * len(s)
        def dfs(i, n):
            if i < n and dp[i] > 0:
                return dp[i]
            if i >= n:
                return 1
            if s[i] not in encodings:
                return 0
            res = dfs(i+1, n)
            if i+1 < n and s[i:i+2] in encodings:
                res += dfs(i+2, n)
            dp[i] = res
            return res
        return dfs(0, len(s))



        

        
            
        