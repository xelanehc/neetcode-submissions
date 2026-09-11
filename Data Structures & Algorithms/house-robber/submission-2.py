class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        n = len(nums)
        T = [0] * n
        T[0] = nums[0]
        T[1] = max(nums[0], nums[1])
        for i in range(2, n):
            T[i] = max(T[i - 2] + nums[i], T[i - 1])
        return T[n - 1]
