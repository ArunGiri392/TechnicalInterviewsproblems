class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # whats the idea here???

        # use greedy appraoch, meaning, if there is a overlapping, i will kind of have to remove one interval and keep another interval. 
        # so which one to remove and which one to keep??? lets dive through an example.
        # remove interval that ends at longer than as compare to interval that ends shorter.


                 
           
        #      ------1------
        # ---2-------   ------3------
        # which  interval do you think on removing would yield the best result??
        # if we remove the interval , 2, then it would still yield the overlapping.
        # but if we remove the interval,1, then we would not have the overlapping right?
        
        # so the idea here is: if we have overlapping then, from two interval, we choose the interval whose endind is smaller/earlier.
        # but why is that? because, if we choose to take a interval that ends earlier, this decreases the probability of of being overlapped with upcoming intervals .
        # taking interval that ends further might decrease this probability.

        
        intervals = sorted(intervals, key=lambda x: x[0])
        end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
                end = min(end, intervals[i][1])
            else:
                end = intervals[i][1]
        return count
    

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals = sorted(intervals, key=lambda x: x[0])

        current_interval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < current_interval[1]:
                # thery are merging
                count += 1
                if current_interval[1] < intervals[i][1]:
                    current_interval = current_interval
                else:
                    current_interval = intervals[i]
            else:
                current_interval = intervals[i]
        return count



   

    # 1----2 2---3
    #            i
    # ci = 1--2

    # c = 2
