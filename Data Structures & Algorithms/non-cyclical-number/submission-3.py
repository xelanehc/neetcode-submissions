class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = 0
        while num not in seen:
            seen.add(num)
            num = 0
            while n:
                digit = n % 10
                num += digit ** 2
                n //= 10
            if num == 1:
                return True
            n = num
        return False
        