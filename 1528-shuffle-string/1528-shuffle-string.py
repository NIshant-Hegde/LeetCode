class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffledString = ""
        temp = [0] * len(s)
        
        for i in range(0, len(s)):
            temp[indices[i]] = s[i]
            
        for i in range(0, len(temp)):
            shuffledString += temp[i]
            
        return shuffledString