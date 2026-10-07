class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            m = l + (r - l) // 2
            
            subarrays = 1
            cur = 0
            for n in nums:
                if cur + n > m:
                    subarrays += 1
                    cur = 0
                cur += n
            
            if subarrays <= k:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res