class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        size = ord('z') + 1
        hmap = [0] * size
        out = 0
        
        for char in stones:
            hmap[ord(char)] += 1
            
        for c in jewels:
            out += hmap[ord(c)]
            
        return out