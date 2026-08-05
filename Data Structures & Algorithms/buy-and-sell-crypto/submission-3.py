class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0 

        for right in range(0, len(prices)):

            if prices[right] < prices[left]:
                left = right
                continue
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        
    

        return max_profit