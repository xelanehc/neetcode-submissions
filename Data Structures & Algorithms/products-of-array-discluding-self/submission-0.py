class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        nums2 = []
        for i in nums:
            nums2.append(i)
        for i in nums:
            nums2.remove(i)
            total = 1
            for j in nums2:
                total *= j
            res.append(total)
            nums2.append(i)
        return res
        