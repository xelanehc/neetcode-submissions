class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 0
        nums += [float('-inf')]

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            else:
                nums[ind] = nums[i]
                ind += 1
        
        return ind