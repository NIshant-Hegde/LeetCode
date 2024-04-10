class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        spaceCount = 0
        out = ""
        
        for chars in s:
            if chars != " ":
                out += chars
            else:
                if spaceCount == k - 1:
                    break
                else:
                    spaceCount += 1
                    out+=" "
        
        return out
        