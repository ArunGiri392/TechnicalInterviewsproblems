class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # THere are several conditions that i need to consider for this problem

        # 1) may be the interval we are trying to add might be on the left side of the interval itself.meaning,
        #   1 --2 , 3 -- 4 , and lets say new interval is -100, 0
        #   so this new interval lies infront of our interval so we just add thisnew interval and add all remaining intervals after this interval.

        #   how do we know this?? 
        #   if the ending of the new interval is smaller than the start of the current interval, then we know, it lies in the left hand side of the current interval.

        #  2) may be the interval we are trying to add might be on the right side of the interval itself.meaning,
        #   1 --2 , 500-- 600 , and lets say new interval is  300 - 400
        #   so this new interval lies infront of our interval so we just add thisnew interval and add all remaining intervals after this interval.

        #   how do we know this?? 
        #   if the start of the new interval is greater than the end of the current interval, then we know, it lies in the right hand side of the current interval.

        
        # 3) but if both this condition does not get satisfied, meaning, the new interval overlapps with the current interval.
        result = []
        for i in range(0, len(intervals)):
            # if end of new interval is smaller than the start of the current interval, meaning it lies on the left side, 
            # so just new interval first, and then add all other remaining intervals.
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                # if the new interval lies ahead of current interval, then already added new interval to our result.so
                # we have to add the reamining intervals, so i is in current interval, so loop through remaining interval and add them
                while i < len(intervals):
                    result.append(intervals[i])
                    i += 1
                return result
            # if start of new interval is greater than the end of the current interval, meaning new interval lies in the right side of the current interval..
            # so in this case, we can add current interval in the result, we will not add the nw interval because, new interval might overlap with the other intervals on the right side.

            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            
            # now, if interval does not lie in the left side of current interval and does not lie on the right side of the current interval?
            # what does it mean?
            # it means, it is overlapping, so we create a new interval and the start of this new interval will be the minimum between the current interval and new interval(given in questoin) and the end of this interrval(new interval we are trying to make) will be the maximum between the end of the current interval and the end of the new interval(given in question)

            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        result.append(newInterval)
        return result



        

        

        
