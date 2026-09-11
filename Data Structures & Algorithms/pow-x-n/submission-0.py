class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        if n == 0:
            return res
        elif n > 0:
            for i in range(n):
                res *= x
        elif n < 0:
            for i in range(-n):
                res /= x
        return res