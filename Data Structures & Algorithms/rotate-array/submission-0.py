class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current = start = 0
        swapped = 0
        n = len(nums)
        k %= n

        while swapped < n:
            current = start
            prev = nums[start]

            while True:
                next_index = (current + k) % n
                nums[next_index], prev = prev, nums[next_index]
                current = next_index
                swapped += 1

                if current == start:
                    break
            
            start += 1