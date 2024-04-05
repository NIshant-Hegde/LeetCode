class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acr = ""
        if len(s) > len(words):
            return False
        
        for word in words:
            acr += word[0]
        
        if acr == s:
            return True
        else:
            return False