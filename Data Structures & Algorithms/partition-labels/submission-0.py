class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for k, v in enumerate(s):
            d[v] = k
        res = []
        size, end = 0, 0
        for i in range(len(s)):
            size += 1
            end = max(end, d[s[i]])
            if i == end:
                res.append(size)
                size = 0
        return res