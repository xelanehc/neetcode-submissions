class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            cur = 0
            while n:
                cur += pow(n % 10, 2)
                n //= 10
            print(cur)
            n = cur
        return False
            