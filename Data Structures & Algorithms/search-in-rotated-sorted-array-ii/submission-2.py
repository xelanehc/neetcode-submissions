class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return True
            
            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m]:
                if nums[r] >= target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1

        return False
        # nums[m] > target:
        #   nums[m] > nums[r] and nums[r] >= target go right
        #   nums[m] > nums[r] and nums[r] < target go left
        #   nums[m] < nums[r] go left
        # nums[m] < target:
        #   nums[m] < nums[l] and nums[l] <= target go left
        #   nums[m] < nums[l] and nums[l] > target go right
        #   nums[m] > nums[l] go right