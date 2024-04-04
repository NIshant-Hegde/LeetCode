class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s), 0, -1):
            t, count = i - 1, 0
            if s[i - 1] != " ":
                while s[t] != " ":
                    count += 1
                    if t <= 0:
                        break
                    else:
                        t -= 1
                break

        return count
