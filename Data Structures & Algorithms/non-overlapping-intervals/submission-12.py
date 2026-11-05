class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []
        cnt = 0
        for i, interval in enumerate(intervals):
            if res and res[-1][1] > interval[0]:
                res[-1] = [min(res[-1][0], interval[0]), min(res[-1][1], interval[1])]
                cnt += 1
            else:
                res.append(interval)
        return cnt