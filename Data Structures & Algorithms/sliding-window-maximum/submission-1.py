class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        resM = float("-infinity")
        l = 0
        res = []
        for r in range(k - 1, len(nums)):
            for i in range(l, r + 1):
                resM = max(resM, nums[i])
            res.append(resM)
            resM = float("-infinity")
            l += 1
        return res
