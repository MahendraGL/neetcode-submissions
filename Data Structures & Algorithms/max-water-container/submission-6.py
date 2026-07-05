class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        n = len(heights)
        i = 0
        j = n-1

        while i<j:
            currVol = min(heights[i], heights[j]) * (j-i)

            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
            max_vol = max(currVol, max_vol)
        return max_vol







        