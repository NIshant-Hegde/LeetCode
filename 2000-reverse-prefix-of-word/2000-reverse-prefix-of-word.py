class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        out = ""
        
        try:
            i = word.index(ch)

            t = word[:(i+1)]
            t = t[::-1]

            out = t + word[i+1:]

            return out
        except:
            return word