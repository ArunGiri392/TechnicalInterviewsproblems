import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # the idea is the smallest i could eat is 1 and the maximum i could eat at 1 hour is maximum bananas at  a pile.
        # then between this numbers .
        # lets say minimum = 1 and maxiumm = 11
        # 1 2 3 4 5 6 7 8 9 10 11
        # i could binary search to find the middle element and see whether it(k) can eat all bananas withink k hours.
        # it it eats, meaning, then we do not have to look for k greater  than it, so but there could be smaller value than that, so right becomes mid - 1.
        # if it is not able to eat within h hours, then we have to increment our left pointers.
        if not piles:
            return 0
        left = 1
        right = max(piles)
        
        
#          
    
        smallest = float("inf")
        while left <= right:
            middle = (left + right) // 2

            if self.can_eat(middle, h, piles) == True:
                smallest = min(smallest,middle)
                right = middle - 1

            else:
                left = middle + 1
        print(smallest)
        return smallest
            
         


    def can_eat(self, k, hours, piles):
      
        time_taken = 0
        for bananas_pile in piles:
            # / gives us exact result and math.ceil always round up . like 2. 4 to 3 but 3.0 stays as 3. that is handled by math.ceil
            # / is used, becasue // automatically rounds down to lower and we do not want that here.
          time_taken += math.ceil((bananas_pile) / k)
        if time_taken > hours:
            return False
        return True

# Time complexity - o(log(max(p)) * o(N))
# where max is the maximum of th piles because we are doing binary search between minimum and maxium and for each k we, iterate through the entire giving piles.
            
           
     
     

       