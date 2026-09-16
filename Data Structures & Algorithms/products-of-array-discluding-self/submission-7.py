class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pref = nums.copy()
        suff = nums.copy()

        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i]

        for i in range(len(nums) - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i]
        
        for i in range(len(nums)):
            if i == 0:
                res[i] = suff[i + 1]
            elif i == len(nums) - 1:
                res[i] = pref[i - 1]
            else:
                res[i] = pref[i - 1] * suff[i + 1]
        
        return res