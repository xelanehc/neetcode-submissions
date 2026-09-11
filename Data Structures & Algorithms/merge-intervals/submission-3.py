class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return None
        if len(intervals) == 1:
            return [intervals[0]]
        intervals.sort()
        last = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if last[1] >= intervals[i][0]:
                last[1] = max(last[1], intervals[i][1])
                last[0] = min(last[0], intervals[i][0])
            else:
                res.append(last)
                last = intervals[i]
        res.append(last)
        return res
