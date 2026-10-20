"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))
        
        time.sort(key=lambda pair: [pair[0], pair[1]])

        res = 0
        cur = 0
        for t in time:
            cur += t[1]
            res = max(res, cur)
        return res