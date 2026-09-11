class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and nums[i - 1] == a:
                continue
            
            b, c = i + 1, len(nums) - 1
            while b < c:
                s = a + nums[b] + nums[c]
                if s == 0:
                    res.append([a, nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while nums[b] == nums[b - 1] and b < c:
                        b += 1
                elif s < 0:
                    b += 1
                else:
                    c -= 1
        
        return res