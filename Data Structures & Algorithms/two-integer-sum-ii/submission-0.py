class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            l = i
            r = len(numbers) - 1
            find = target - n
            while r > l:
                if numbers[r] == find:
                    return [l + 1, r + 1]
                r -= 1
            