class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            cur = 0
            val = i
            for j in range(32):
                if val & 1:
                    cur += 1
                val >>= 1
            res[i] = cur
        return res
