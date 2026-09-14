class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums):
            if len(nums) == 1:
                return nums
            mid = len(nums) // 2
            left = merge(nums[:mid])
            right = merge(nums[mid:])
            i, j = 0, 0
            ret = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    ret.append(left[i])
                    i += 1
                else:
                    ret.append(right[j])
                    j += 1
            
            while i < len(left):
                ret.append(left[i])
                i += 1
            while j < len(right):
                ret.append(right[j])
                j += 1

            return ret

        return merge(nums)