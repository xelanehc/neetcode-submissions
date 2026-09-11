class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        return fast == 1
        
    def sumOfSquares(self, n):
        res = 0
        while n:
            digit = n % 10
            res += digit ** 2
            n //= 10
        return res
        