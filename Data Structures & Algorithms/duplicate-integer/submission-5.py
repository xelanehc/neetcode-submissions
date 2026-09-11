class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            s.add(n)
        return len(s) != len(nums)