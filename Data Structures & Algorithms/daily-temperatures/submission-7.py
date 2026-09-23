class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for t in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[t]:
                i, v = stack.pop()
                res[i] = t - i

            stack.append([t, temperatures[t]])

        return res