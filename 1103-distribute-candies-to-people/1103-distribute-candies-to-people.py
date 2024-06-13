class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        handedOut, i, t, k = 0, 0, 0, 0
        remaining = candies
        
        out = [0] * num_people
        
        while remaining > 0:
            handedOut += 1
            
            if i == len(out):
                i = 0
                k += 1
                t = k * len(out)
            
            if remaining < (t + 1):
                out[i] += remaining
            else:
                out[i] += t + 1
                
            handedOut = sum(out)
            remaining = candies - handedOut
            
            i+=1
            t+=1
            
        return out