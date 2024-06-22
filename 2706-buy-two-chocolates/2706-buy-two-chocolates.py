class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sortedPrices = sorted(prices)
        
        if (sortedPrices[0] + sortedPrices[1]) > money:
            return money
        else:
            return money - (sortedPrices[0] + sortedPrices[1])