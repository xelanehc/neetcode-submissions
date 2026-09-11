class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        power = 0
        num = 0
        for i in range(len(digits) - 1, -1, -1):
            num += (digits[i] * (10 ** power))
            power += 1
        num += 1
        res = []
        while num:
            digit = num % 10
            res.insert(0, digit)
            num //= 10
        return res