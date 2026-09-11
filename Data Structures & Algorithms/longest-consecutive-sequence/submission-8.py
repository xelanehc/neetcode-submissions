class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        d = {}
        for n in nums:
            d[n] = 1
        res = 1
        for i in sorted(d.keys()):
            if i - 1 in d:
                d[i] = d[i - 1] + 1
                res = max(res, d[i - 1] + 1)
        return res