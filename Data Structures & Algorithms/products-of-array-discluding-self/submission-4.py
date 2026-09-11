class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i - 1])
        suffix = [1]
        for i in range(1, len(nums)):
            suffix.append(suffix[i - 1] * nums[len(nums) - i])
        suffix = suffix[::-1]
        ret = []
        for i in range(len(nums)):
            ret.append(prefix[i] * suffix[i])
        return ret
