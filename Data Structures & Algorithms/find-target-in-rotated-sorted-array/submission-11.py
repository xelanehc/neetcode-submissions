class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                if nums[m] > nums[r] and nums[r] >= target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] < nums[l] and nums[l] <= target:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1
        
        # nums[m] > target
        #   if nums[m] > nums[r] and nums[r] >= target go right
        #   if nums[m] > nums[r] and nums[r] < target go left
        #   if nums[m] < nums[r] then go left
        # nums[m] < target
        #   if nums[m] < nums[l] and nums[l] <= target go left
        #   if nums[m] < nums[l] and nums[l] > target go right
        #   if nums[m] > nums[l] then go right