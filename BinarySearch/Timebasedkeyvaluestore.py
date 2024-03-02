class TimeMap:
  # use binary search to find the element 
  # if it is present, return the location where it is positioed(mid)
  # if not, return the most nearestto that give timestamp(use another binary search.)
    def __init__(self):
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        listsofvalue = self.hashmap[key]
        mid = self.binarysearch(listsofvalue, timestamp)
        # if timestamp is not present and also , its nereast time stamp is not present, then we get mid as -infinity. so checking that condition here.
        if mid ==  float('-inf'):
            return ""
        return listsofvalue[mid][0]
    

    def binarysearch(self, lists, timestamp):
        left = 0
        right = len(lists) - 1

    #binary search to find the whethter time stamp is present or not.
        while left <= right:
            mid = (left + right) // 2
            if lists[mid][1] == timestamp:
                return mid
            elif timestamp > lists[mid][1]:
                left = mid + 1
            else:
                right = mid - 1
        
        # if time stamp is not present, then we need to find the nearest timestamp, should be smaller, not greater.
        # code to find the most nearest of given timestamp.

        left = 0
        right = len(lists) - 1
        smallest = float('-inf')


        while left <= right:
            mid = (left + right) // 2
          
            if lists[mid][1] < timestamp:
                # we should calcualte the max, we go on right side, so right index will be greater, and if it is nearere, we consdier, thsi so take max.
                smallest = max(smallest, mid)
                left = mid + 1
            else:
                right = mid - 1
        return smallest


        



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)