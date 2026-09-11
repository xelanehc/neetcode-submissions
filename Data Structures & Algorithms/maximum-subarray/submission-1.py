class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        prefixSum = 0
        for n in nums:
            if prefixSum < 0:
                prefixSum = 0
            prefixSum += n
            res = max(res, prefixSum)
        return res