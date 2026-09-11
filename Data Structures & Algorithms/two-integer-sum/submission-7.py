class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, v in enumerate(nums):
            comp = target - v
            if comp in d:
                return [d[comp], i]
            d[v] = i
        
        return False