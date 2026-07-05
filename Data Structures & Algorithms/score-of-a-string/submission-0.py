class Solution:
    def scoreOfString(self, s: str) -> int:
        l = 0
        n = len(s)
        res = 0

        for r in range(1, n):
            sub = abs(ord(s[l]) - ord(s[r]))
            res += sub
            l+=1
        return res