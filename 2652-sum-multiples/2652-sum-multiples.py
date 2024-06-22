class Solution:
    def sumOfMultiples(self, n: int) -> int:
        l = []
        i = 0
        
        while i <= n:
            if ((i%3)==0) or ((i%5)==0) or ((i%7)==0):
                l.append(i)

            i+=1
                
        return sum(l)