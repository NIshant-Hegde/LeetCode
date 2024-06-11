class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        else:
            l = []
            left, right = (-n), n
            if n%2==0:
                for i in range(0, n):
                    if (i < (n//2)):
                        l.append(left + i)
                    else:
                        l.append(i + 1)
            else:
                for i in range(0, n):
                    if (i < (n//2)):
                        l.append(left + i)
                    elif (i > (n//2)):
                        l.append(i + 1)
                    else:
                        l.append(0)
                        
            return l
                    
                