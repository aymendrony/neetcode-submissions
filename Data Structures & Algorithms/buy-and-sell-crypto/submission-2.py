class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        L = 0  
        for R in range(1, len(prices)):
            if prices[R] < prices[L]:
                L = R  
            else:
                profit = prices[R] - prices[L]
                max_profit = max(max_profit, profit)
        return max_profit
