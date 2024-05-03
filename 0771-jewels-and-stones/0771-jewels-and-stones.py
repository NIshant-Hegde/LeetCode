class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hmp = [0] * 150

        for s in stones:
            hmp[ord(s)] += 1

        count = 0
        for j in jewels:
            print(j, ord(j))
            count += hmp[ord(j)]

        return count
        