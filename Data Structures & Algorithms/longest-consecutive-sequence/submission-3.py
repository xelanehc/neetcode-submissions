class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ret = 0
        for num in nums:
            if (num-1) not in nums:
                streak = 1
                while num + streak in nums:
                    streak += 1
                ret = max(streak,ret)
        return ret