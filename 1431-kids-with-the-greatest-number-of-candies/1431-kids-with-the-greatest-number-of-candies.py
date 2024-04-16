class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = candies[0]
        out = []
        
        for candy in candies:
            if candy > greatest:
                greatest = candy
                
        for candy in candies:
            if (candy + extraCandies) >= greatest:
                out.append(True)
            else:
                out.append(False)
        
        return out
        