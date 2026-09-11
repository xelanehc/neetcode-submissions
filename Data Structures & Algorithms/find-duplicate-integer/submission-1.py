class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = set()
        for n in nums:
            if n in d:
                return n
            else:
                d.add(n)
        return -1