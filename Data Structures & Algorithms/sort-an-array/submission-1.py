class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) == 1:
                return nums.copy()
            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            return merge(left, right)

        def merge(left, right):
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

        return mergeSort(nums)