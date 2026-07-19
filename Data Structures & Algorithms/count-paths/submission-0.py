class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = m*[n*[-1]]
        dp = [[-1] * n for _ in range(m)]
        print(len(dp), len(dp[0]))
        def recurse(i, j):
            if i == 0 and j == 0:
                return 1
            if i <0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = recurse(i, j-1) + recurse(i-1, j)
            return dp[i][j]
        return recurse(m-1, n-1)
            

        