def permute( nums):
        
        def backtracking(result, templist, nums):
            
            # base case
            if len(templist) == len(nums):
                result.append(list(templist))
                return

            for num in nums:
                if num in templist:
                    continue
                
                templist.append(num)

                backtracking(result, templist, nums)
                templist.pop()

        

        result = []
        templist = []
        backtracking(result, templist, nums)
        return result
print(permute([1,2,3]))

# Time Complexity: O(N*N!) Note that there are N! permutations and it requires O(N) time to print a permutation.
# Auxiliary Space: O(r – l)