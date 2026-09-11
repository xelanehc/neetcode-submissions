class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minMap = defaultdict(lambda: float('inf'))

        for i in intervals:
            for j in range(i[0], i[1] + 1):
                minMap[j] = min(minMap[j], i[1] - i[0] + 1)
        
        res = []
        for q in queries:
            res.append(minMap[q] if minMap[q] != float('inf') else -1)
        
        return res