class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [float('inf')] * len(queries)

        for q in range(len(queries)):
            for i in intervals:
                if queries[q] >= i[0] and queries[q] <= i[1]:
                    res[q] = min(res[q], i[1] - i[0] + 1)
            if res[q] == float('inf'):
                res[q] = -1
        
        return res
        
