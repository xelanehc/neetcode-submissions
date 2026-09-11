class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        for i in range(len(nums)):
            for j in range(i + 1):
                prod = 1
                for k in range(j, i + 1):
                    prod *= nums[k]
                res = max(res, prod)
        
        return res