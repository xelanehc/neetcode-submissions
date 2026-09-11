class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        p = 0
        n1 = 0
        for i in range(len(num1) - 1, -1, -1):
            digit = ord(num1[i]) - ord('0')
            n1 += digit * pow(10, p)
            p += 1
        
        p = 0
        n2 = 0
        for i in range(len(num2) - 1, -1, -1):
            digit = ord(num2[i]) - ord('0')
            n2 += digit * pow(10, p)
            p += 1
        
        prod = n1 * n2
        res = ""

        if prod == 0:
            return "0"

        while prod:
            digit = prod % 10
            char = chr(digit + ord('0'))
            res = char + res

            prod //= 10

        return res