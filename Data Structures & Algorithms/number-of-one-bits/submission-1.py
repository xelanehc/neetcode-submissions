class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            cur = n & 1
            if cur:
                res += 1
            n >>= 1
        return res