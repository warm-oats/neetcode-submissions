class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        max_profit = 0

        while l < len(prices) and r < len(prices):
            if len(prices) == 1:
                return 0

            if prices[r] - prices[l] <= 0:
                l = r
                r += 1
            else:
                current_profit = prices[r] - prices[l]
                max_profit = max(max_profit, current_profit)

                r += 1
        
        return max_profit