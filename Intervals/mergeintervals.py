class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # for merging the intervals, if the start of the interval is not sorted , then it would be extremely difficult for us figure out where to insert
        # and it could get more complex as we go on.
        # so we want to sort the given intervals based on the start of each interval.

        intervals = sorted(intervals, key=lambda x: x[0])
        # so basically what i am doing is: keeping first interval as new interval and 
        #  startinf from 2nd interval. so if 2nd interval overlaps with first interval. increase their range, by calculating the max and min,
        # if 2nd interval does not overlaps, then append new_interval(previous) into our final answer, cause we know at this point there isnot merging .


        new_interval = intervals[0]
        result = []
        for i in range(1, len(intervals)):
            # if current_itnerval either lies in the left side or the right side, it means it does not overalap
            current_interval = intervals[i]
            # here we are checking if our current interval lies on the right side of previous(newitnerval) then, it means they do not merge.
            #
            if current_interval[0] > new_interval[1]:
                result.append(new_interval)
                # so for next iteration, making current interval as the new interval.
                new_interval = current_interval


            else:
                # if it overlaps right??
                # then we keep on extending its range.
                new_interval = [min(new_interval[0], current_interval[0]), max(new_interval[1], current_interval[1])]
        # here we need to append the new interval to our final response.
        result.append(new_interval)
        return result
