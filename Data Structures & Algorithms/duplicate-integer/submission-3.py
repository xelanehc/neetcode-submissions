class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for n in nums:
            print(d[n])
            d[n] += 1
            print(d[n])
        for k in d.keys():
            if d[k] > 1:
                return True
        return False