class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pointer_left = 0
        pointer_right = 1
        max_profit = 0

        while pointer_left < len(prices) and pointer_right < len(prices):
            if len(prices) == 1:
                return 0

            if prices[pointer_left] > prices[pointer_right]:
                pointer_left += 1
                pointer_right = pointer_left + 1
            else:
                max_profit = max(max_profit,prices[pointer_right]-prices[pointer_left])
                pointer_right += 1
        
        return max_profit