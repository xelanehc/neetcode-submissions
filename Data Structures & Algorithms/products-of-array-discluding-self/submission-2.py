class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefixes[i] = 1
            else:
                prefixes[i] = prefixes[i-1] * nums[i-1]
        postfixes = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfixes[i] = 1
            else:
                postfixes[i] = nums[i + 1] * postfixes[i + 1]
        for i in range(len(nums)):
            nums[i] = prefixes[i] * postfixes[i]
        return nums
            

        