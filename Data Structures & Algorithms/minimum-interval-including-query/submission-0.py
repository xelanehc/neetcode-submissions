class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [-1] * len(queries)
        for q in range(len(queries)):
            m = float('inf')
            for i in intervals:
                if i[1] >= queries[q] and i[0] <= queries[q]:
                    m = min(m, i[1] - i[0] + 1)
            if m != float('inf'):
                res[q] = m
        return res
