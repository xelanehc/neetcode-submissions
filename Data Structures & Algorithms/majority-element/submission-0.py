class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        ret = 0
        m = 0
        for k in d.keys():
            if d[k] > m:
                m = d[k]
                ret = k
        
        return ret