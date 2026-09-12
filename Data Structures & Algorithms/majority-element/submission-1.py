class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        ret = 0
        m = 0

        for n in nums:
            d[n] = d.get(n, 0) + 1
            if d[n] > m:
                m = d[n]
                ret = n
        
        return ret
