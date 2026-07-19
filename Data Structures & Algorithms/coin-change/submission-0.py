class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp =[float("inf") for j in range(amount+1)]
        for c in coins:
            if c <= amount:
                dp[c] = 1
        for j in range(amount + 1):
            for i in range(len(coins)):
                c = coins[i]
                if j >= c:
                    dp[j] = min(1 + dp[j-c], dp[j])
        ans = dp[amount]
        if ans != float("inf"):
            return ans
        return -1


        