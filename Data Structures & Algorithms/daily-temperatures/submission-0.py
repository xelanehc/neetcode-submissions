class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            j = i + 1
            found = False
            while j < len(temperatures):
                if temperatures[i] < temperatures[j]:
                    res.append(j - i)
                    found = True
                    break
                j += 1
            if not found:
                res.append(0)
        return res