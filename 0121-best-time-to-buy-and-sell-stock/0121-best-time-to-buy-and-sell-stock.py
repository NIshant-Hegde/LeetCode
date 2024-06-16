class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp, rp = 0, 1
        maxProfit = 0
        
        while rp < len(prices):
            profit = prices[rp] - prices[lp]
            if profit > 0:
                maxProfit = max(profit, maxProfit)
            else:
                lp = rp
            rp+=1
        
        return maxProfit
            