class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            count = 0
            cur = i
            for j in range(32):
                bit = cur & 1
                count += bit
                cur >>= 1
            res.append(count)
        return res