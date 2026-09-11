class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for n in range(len(nums)):
            res ^= nums[n]
            res ^= n
        return res