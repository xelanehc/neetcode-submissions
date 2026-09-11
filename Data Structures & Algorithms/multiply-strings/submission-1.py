class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = [], []
        for i in num1:
            n1.append(ord(i) - ord('0'))
        for i in num2:
            n2.append(ord(i) - ord('0'))
        power = 0
        num1, num2 = 0, 0
        for i in range(len(n1) - 1, -1, -1):
            num1 += n1[i] * (10 ** power)
            power += 1
        power = 0
        for i in range(len(n2) - 1, -1, -1):
            num2 += n2[i] * (10 ** power)
            power += 1
        total = num1 * num2
        if total == 0:
            return "0"
        res = []
        while total:
            digit = total % 10
            res.insert(0, chr(ord('0') + digit))
            total //= 10
        return "".join(res)