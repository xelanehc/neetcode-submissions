class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        for key in d.keys():
            if d[key] >= 2:
                return key
        return -1