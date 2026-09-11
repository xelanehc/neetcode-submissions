class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = []
        for i, v in enumerate(nums):
            if v > 0: #anything past 0 will sum to over 0
                break
            if i > 0 and v == nums[i - 1]: #skip over terms that are consecutively equal
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = v + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    ret.append([v, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return ret