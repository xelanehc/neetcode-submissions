class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        print(intervals)
        fixed = [intervals[0]]
        res = 0

        for i in intervals[1:]:
            lastEnd = fixed[-1][1]
            if i[0] < lastEnd:
                fixed[-1][1] = min(lastEnd, i[1])
                res += 1
            else:
                fixed.append(i)
        return res