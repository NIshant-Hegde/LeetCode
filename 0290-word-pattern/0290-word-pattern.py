class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hmap = [0] * 26

        words = []
        temp = ""

        for c in s:
            if c != " ":
                temp += c
            else:
                words.append(temp)
                temp = ""

        words.append(temp)

        if len(words) == len(pattern):
            for c, word in enumerate(words):
                if hmap[ord(pattern[c]) - 97] == 0:
                    if word not in hmap:
                        hmap[ord(pattern[c]) - 97] = word
                    else:
                        return False
                elif hmap[ord(pattern[c]) - 97] != word:
                    return False

            return True
        else:
            return False
            
        