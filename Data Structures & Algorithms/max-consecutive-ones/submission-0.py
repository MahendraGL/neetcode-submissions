class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        curMax = 0
        for num in nums:
            if num == 1:
                curMax +=1
                c = max(c, curMax)
            elif num!=1:
                curMax = 0
                c = max(c, curMax)
        return c

