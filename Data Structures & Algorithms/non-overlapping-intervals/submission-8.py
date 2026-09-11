class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        prevEnd = float('inf')

        for i in range(len(intervals)):
            if prevEnd == float('inf'):
                prevEnd = intervals[i][1]
            elif prevEnd > intervals[i][0]:
                count += 1
                prevEnd = min(prevEnd, intervals[i][1])
            else:
                prevEnd = intervals[i][1]
        
        return count