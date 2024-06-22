class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        l1, l2 = 0, 0
        
        l1 = min(prices)
        
        prices[prices.index(l1)] = 1000
        
        l2 = min(prices)
        
        if (l1 + l2) > money:
            return money
        else:
            return money - (l1 + l2)