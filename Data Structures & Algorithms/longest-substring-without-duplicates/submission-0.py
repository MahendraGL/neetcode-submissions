class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        n = len(s)

        l = 0
        longest = 0

        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            w= (r-l) + 1
            longest = max(longest, w)
            charSet.add(s[r])

        return longest



        