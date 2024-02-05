def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()

        i = 0
        j = 0
        meeting_going_on = 0
        max_count = 0

        # i iterate through start times.
        # j iterate through end times.
        # start times would end earlier than end times.
        # so while i < len(start) is used.

        while i <  len(start):
            if start[i] < end[j]:
                meeting_going_on += 1
                i += 1
            else:
                meeting_going_on -= 1
                j += 1
            max_count = max(max_count, max)
        return max_count
        
        # Time complexity - o(N)
        # Space complexity - o(N)