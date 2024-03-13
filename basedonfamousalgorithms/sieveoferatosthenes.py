class Solution:
    def countPrimes(self, n: int) -> int:
        # SieveOfEratosthenes
        if n < 2:
            return 0
        primes = [True] * n                                                                                                                                                       
        # setting 0 and 1 as False as they are never Prime numbers.
        primes[0] = False
        primes[1] = False
        # print(primes)

        for i in range(2, n):
            if primes[i]:
                # its a prime, and change all the multiples of this to False.
                # i * i because, if i is 2, then we start from 4 
                # we go up to n,
                # and the gap should be n, meaning, for i =2,first, we get, 4, then, 6, 8, the gap is 2 ie i
                # for i = 3, we get, 6, 9, 12, ie gap is i (3)
                for multiple in range(i * i , n, i):
                    primes[multiple] = False
        
        # at end, whatever is true, those are the prime numbers.
        count = 0
        for boolean in primes:
            if boolean:
                count += 1
        return count
# Time complexity --  O(n * log(log(n))).

    #     count = 0
    #     for i in range(2, n):
    #         if self.is_prime(i):
    #             count += 1
    #     return count
    



    # def is_prime(self, number):
    #     # 2 is always prime.
    #     if number == 2:
    #         return True
    #     # any even number except 2 will never be prime number.
    #     if number % 2 == 0:
    #         return False
        
    #     # just going up to square root of number.
    #     for i in range(2, int(number**0.5) + 1):
    #         if number % i == 0:
    #             return False
    #     return True

    #     # Time compleixty -- square root of N.
