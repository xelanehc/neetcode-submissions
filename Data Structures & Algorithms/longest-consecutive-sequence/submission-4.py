class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        streak = 0
        for i in nums:
            if (i-1) not in nums:
                length = 1
                while (i + length) in nums:
                    length+=1
                streak = max(streak, length)
        return streak