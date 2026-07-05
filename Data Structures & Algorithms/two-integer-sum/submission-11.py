class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}

        for i,n in enumerate(nums):
            diff = target - n

            if diff in idx:
                return [idx[diff], i]
            
            idx[n] = i


'''


        l = len(nums)

        for i in range(l):
            for j in range(l):
                if i!=j:
                    if nums[i]+nums[j]== target:
                        return [i, j]
'''