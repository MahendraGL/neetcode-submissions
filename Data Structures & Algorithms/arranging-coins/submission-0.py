class Solution:
    def arrangeCoins(self, n: int) -> int:

        l, r = 1, n
        row = 0

        while l<=r:
            mid = (l+r) // 2
            c = (mid * (mid+1)) // 2

            if c>n:
                r = mid - 1
            else:
                l = mid + 1
                row = max(row, mid)
        return row




