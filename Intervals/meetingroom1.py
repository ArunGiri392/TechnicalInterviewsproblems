
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        if len(intervals) == 1:
            return True

        current_interval = intervals[0]

        for i in range(1,len(intervals)):
            if intervals[i][start] < current_interval[end]:
                return False
            current_interval = intervals[i]
        return True

