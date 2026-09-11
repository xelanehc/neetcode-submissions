class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for n in range(len(nums)):
            res ^= nums[n]
            res ^= n
        res ^= len(nums)
        return res