class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if (n & 1):
                res += pow(2, (32 - i - 1))
            n >>= 1
        return res