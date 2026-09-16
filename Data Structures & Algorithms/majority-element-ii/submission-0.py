class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        limit = len(nums) / 3

        for n in nums:
            d[n] += 1
        
        res = []
        for k, v in d.items():
            if v > limit:
                res.append(k)
        
        return res