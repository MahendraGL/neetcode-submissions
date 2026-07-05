class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}

        for i, n in enumerate(nums):
            idx[n] = i
        
        for i, n in enumerate(nums):
            d = target - n

            if d in idx and idx[d]!=i:
                return [i, idx[d]]
        return []


'''


        l = len(nums)

        for i in range(l):
            for j in range(l):
                if i!=j:
                    if nums[i]+nums[j]== target:
                        return [i, j]
'''