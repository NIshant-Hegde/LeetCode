class Solution:
    def sumOfMultiples(self, n: int) -> int:
        hmap = [0] * 10000
        i = 1
        
        while i <= n:
            if ((i%3)==0) or ((i%5)==0) or ((i%7)==0):
                print(i)
                hmap[i] = 1

            i+=1
        
        out = 0
        for i, ele in enumerate(hmap):
            if ele == 1:
                out += i
                
        return out