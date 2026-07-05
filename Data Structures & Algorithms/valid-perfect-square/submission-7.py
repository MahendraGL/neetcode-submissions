class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num

        if num==1:
            return True

        while l<=r:
            mid = (l+r) // 2

            sq = mid*mid

            if sq == num:
                return True
            elif sq>num:
                r = mid - 1
            else:
                l=mid + 1
        return False        
        