class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in s:
                j = n + 1
                while j in s:
                    j += 1
                res = max(res, j - n)
        
        return res