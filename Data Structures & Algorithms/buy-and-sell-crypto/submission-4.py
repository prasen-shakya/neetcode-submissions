class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0

        for r in range(len(prices)):
            buy = prices[l]
            sell = prices[r]

            print(buy, sell)
            if sell < buy:
                l = r
                continue
            
            res = max(sell - buy, res)

        return res