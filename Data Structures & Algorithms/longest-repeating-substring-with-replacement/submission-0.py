class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        n = len(s)
        freq = 0
        res = 0
        
        for r in range(n):
            count[s[r]] = count.get(s[r],0) + 1
            freq = max(freq, count[s[r]])

            while (r-l+1) - freq > k:
                count[s[l]]-=1            
                l+=1
            res = max(res, r-l+1)
        return res