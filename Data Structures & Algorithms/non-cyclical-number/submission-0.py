class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = n
        total = 0
        while cur != 1 and cur not in seen:
            seen.add(cur)
            while cur:
                digit = cur % 10
                total += int(pow(digit, 2))
                cur //= 10
            cur = total
            total = 0
            
        return cur == 1