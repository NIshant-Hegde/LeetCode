class Solution:
    def pivotInteger(self, n: int) -> int:
        '''
        Brute-Force: Comparing an element's left sum and right sum
        if n == 1:
            return 1
        else:
            l = [i for i in range(1, n + 1)]

            for i in range(1, len(l)):
                if sum(l[0:(i+1)]) == sum(l[i:(len(l) + 1)]):
                    return i+1

            return -1
        '''
        '''
        #Two pointer approach
        lp, rp = 1, n
        lsum, rsum = 1, n
        
        if n == 1:
            return 1
        else:
            while lp < rp:
                if lsum < rsum:
                    lp += 1
                    lsum += lp
                else:
                    rp -= 1
                    rsum += rp

                if (lsum == rsum) and (lp == rp):
                    return lp

            return -1
        '''
        
        #Math based approach
        #By equating the sum of elements from 1 to x and x to n
        #we find out that x^2 is equal to sum of elements from 1 to n
        
        nsum = (n * (n + 1))//2
        x = int(nsum**(0.5))
        
        if (x*x == nsum):
            return x
        
        return -1
        