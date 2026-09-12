class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ret = 0

        for n in nums:
            if count == 0:
                ret = n
            count += (1 if n == ret else -1)

        return ret