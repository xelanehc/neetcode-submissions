class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, v in enumerate(s):
            last[v] = i
        
        res = []
        size = 0
        end = 0
        for i, v in enumerate(s):
            end = max(end, last[v])
            size += 1
            
            if i == end:
                res.append(size)
                size = 0
        
        return res