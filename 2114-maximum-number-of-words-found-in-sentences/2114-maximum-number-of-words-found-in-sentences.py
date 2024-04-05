class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        spaceCount = []
        
        #Extract words
        for sentence in sentences:
            spaceCount.append(sentence.count(" "))
        
        return max(spaceCount) + 1
            