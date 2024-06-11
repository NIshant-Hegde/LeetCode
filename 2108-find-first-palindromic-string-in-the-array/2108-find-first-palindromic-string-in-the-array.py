def isPalindrome(word):
    return word == word[::-1]

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if isPalindrome(word):
                return word
        
        return ""