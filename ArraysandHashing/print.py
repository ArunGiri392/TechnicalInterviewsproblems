
def isHappy( n: int) -> bool:
        original_number = n * n
        
        while n != 1:
            sum = 0
            while n > 0:
                digit = n % 10
                n = n //10
                sum = sum +  digit * digit
            print(sum)

            if sum == 1:
                return True
                
            if sum == original_number:
                return False

            n = sum
print(isHappy(2))