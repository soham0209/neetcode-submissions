class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)] 
        dp[len(s1)][len(s2)] = True
        m, n = len(s1), len(s2)
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < m and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < n and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
                
        return dp[0][0]
                

                
        
        