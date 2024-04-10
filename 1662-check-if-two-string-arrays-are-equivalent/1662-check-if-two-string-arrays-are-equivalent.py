class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = " "
        s2 = " "
        
        for w1 in word1:
            s1 += w1
            
        for w2 in word2:
            s2 += w2
            
        if len(s1) != len(s2):
            return False
        else:
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    return False
            return True