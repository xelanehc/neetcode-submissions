class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        lastEnd = intervals[0][1]
        res = 0

        for i in intervals[1:]:
            if i[0] < lastEnd:
                lastEnd = min(lastEnd, i[1])
                res += 1
            else:
                lastEnd = i[1]
        return res