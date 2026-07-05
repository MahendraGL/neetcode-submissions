class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = n//2
        hashMap = {}


        for i in range(n):
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1
        for key, value in hashMap.items():
            if value > freq:
                return key