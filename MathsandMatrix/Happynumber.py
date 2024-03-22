class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        visit = set()
        
        while n != 1:
            sum = 0
            while n > 0:
                digit = n % 10
                n = n //10
                sum = sum +  digit * digit

            if sum == 1:
                return True
            
            if sum in visit:
                return False
            
            if sum not in visit:
                visit.add(sum)
            

            n = sum
        