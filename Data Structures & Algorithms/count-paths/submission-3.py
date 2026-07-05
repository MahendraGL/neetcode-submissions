class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Space optimized

        dpRow = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dpRow[j]+=dpRow[j-1]
        
        return dpRow[n-1]

