class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in nums:
            if n - 1 in s:
                continue
            l = 0
            cur = n
            while cur in s:
                l += 1
                cur += 1
            res = max(res, l)
        
        return res