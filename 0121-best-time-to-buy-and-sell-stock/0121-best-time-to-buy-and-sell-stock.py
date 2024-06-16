class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp, rp = 0, 1
        maxProfit = 0
        
        while rp < len(prices):
            if prices[rp] > prices[lp]:
                maxProfit = max(prices[rp] - prices[lp], maxProfit)
            else:
                lp = rp
            rp+=1
        
        return maxProfit
            