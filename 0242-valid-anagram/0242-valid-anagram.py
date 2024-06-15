class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            map1, map2 = ([0] * 26), ([0] * 26)
            
            for i in range(len(s)):
                map1[ord(s[i]) - ord("a")] += 1
                map2[ord(t[i]) - ord("a")] += 1

            for j in range(len(map1)):
                if map1[j] != map2[j]:
                    return False
            
            return True