class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            l = [i for i in range(1, n + 1)]

            for i in range(1, len(l)):
                if sum(l[0:(i+1)]) == sum(l[i:(len(l) + 1)]):
                    return i+1

            return -1