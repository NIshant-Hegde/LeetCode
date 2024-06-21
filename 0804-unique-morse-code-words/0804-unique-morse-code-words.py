class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        mCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = []
        
        for word in words:
            temp = ""
            for c in word:
                temp += str(mCode[(ord(c) - ord('a'))])

            res.append(temp)
        
        return len(set(res))