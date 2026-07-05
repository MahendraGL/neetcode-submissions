class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        h1, h2 = 0, 0
        for n in nums:
            newRob = max(h1+n, h2)
            h1=h2
            h2=newRob
        return h2
        