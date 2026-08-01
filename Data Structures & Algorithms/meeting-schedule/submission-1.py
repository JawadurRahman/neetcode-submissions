"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        last_end = None
        intervals.sort(key=lambda i: i.start)

        for interval in intervals:
            if last_end != None and interval.start < last_end:
                return False
            last_end = interval.end

        return True