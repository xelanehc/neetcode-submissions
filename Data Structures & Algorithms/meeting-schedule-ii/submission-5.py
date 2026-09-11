"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()

        i, j = 0, 0
        res = 0
        count = 0

        while i < len(intervals):
            if start[i] < end[j]:
                count += 1
                i += 1
            elif start[i] >= end[j]:
                count -= 1
                j += 1
            res = max(res, count)
        
        return res