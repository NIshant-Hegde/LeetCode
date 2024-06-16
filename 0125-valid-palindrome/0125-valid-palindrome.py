class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        else:
            s = s.lower()
            t=""

            for c in s:
                if ((ord('0') <= ord(c)) and (ord(c) <= ord('9'))) or ((ord('a') <= ord(c)) and (ord(c) <= ord('z'))):
                    t+=c

            lp, rp = 0, len(t) - 1

            while lp <= rp:
                if t[lp] != t[rp]:
                    return False
                lp+=1
                rp-=1

            return True