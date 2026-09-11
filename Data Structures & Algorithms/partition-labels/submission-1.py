class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for k, v in enumerate(s):
            lastIndex[v] = k
        res = []
        length, end = 0, 0
        for i, c in enumerate(s):
            length += 1
            end = max(end, lastIndex[c])
            if i == end:
                res.append(length)
                length = 0
        return res