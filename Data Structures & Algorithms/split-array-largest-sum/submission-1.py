class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSums = [0] * (n + 1)
        for i in range(n):
            prefixSums[i + 1] = nums[i] + prefixSums[i]
        
        def canSplit(largest):
            subarrays = 0
            i = 0
            while i < n:
                l, r = i + 1, n
                while l <= r:
                    m = l + (r - l) // 2
                    if prefixSums[m] - prefixSums[i] <= largest:
                        l = m + 1
                    else:
                        r = m - 1
                subarrays += 1
                i = r
                if subarrays > k:
                    return False
            return True
        
        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            m = l + (r - l) // 2
            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res