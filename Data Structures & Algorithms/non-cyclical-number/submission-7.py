class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            n = self.digitSum(n)
            
        return False

    def digitSum(self, n):
        res = 0
        while n != 0:
            digit = n % 10
            res += digit ** 2
            n //= 10
        return res