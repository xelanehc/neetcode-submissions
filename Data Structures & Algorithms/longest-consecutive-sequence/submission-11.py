class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            if n - 1 in nums:
                continue
            cur = 1
            while n + cur in nums:
                cur += 1
            res = max(res, cur)
        
        return res
            
            