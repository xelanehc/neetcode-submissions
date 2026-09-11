class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1 = []
        l2 = []
        for n1 in num1:
            l1.append(ord(n1) - ord('0'))
        for n2 in num2: 
            l2.append(ord(n2) - ord('0'))
        n1 = 0
        p = 0
        for i in range(len(l1) - 1, -1, -1):
            n1 += l1[i] * pow(10, p)
            l1.pop()
            p += 1
        n2 = 0
        p = 0
        for i in range(len(l2) - 1, -1, -1):
            n2 += l2[i] * pow(10, p)
            p += 1
        
        product = n1 * n2
        res = []
        if product == 0:
            return "0"
        while product:
            digit = product % 10
            res.insert(0, chr(digit + ord('0')))
            product //= 10
        return "".join(res)
