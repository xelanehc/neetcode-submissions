class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.digitSum(n)
        while slow != fast:
            fast = self.digitSum(fast)
            fast = self.digitSum(fast)
            slow = self.digitSum(slow)

        return fast == 1

    def digitSum(self, n):
        res = 0
        while n != 0:
            digit = n % 10
            res += digit ** 2
            n //= 10
        return res