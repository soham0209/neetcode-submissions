class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 2:
            return profit
        buy_price = prices[0]
        for p in prices[1:]:
            profit = max(profit, p - buy_price)
            buy_price = min(buy_price, p)
        return profit

        