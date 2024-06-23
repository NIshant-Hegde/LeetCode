class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hmap = [0] * 26
        
        for word in words:
            for c in word:
                hmap[ord(c) - ord('a')] += 1
                
        for ele in hmap:
            if ele % len(words) != 0:
                return False
        
        return True