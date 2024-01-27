class Solution(object):
 
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # At each point there is two choices:
        # either to take or not take.
        # 1) if i take that value, then i could i also take it again and again, so i do not increase index there.
        # 2) if i do not take that value, i go to next index and there is no change in total or temporary array.

        result = []
        def dfs(index,current,total):
            if total == target:
                result.append(current.copy())
                return 
            # even if i decided to take value, then it at any  point:
            # current toal > target or index becomes greater than len(canidates), there is not point on exploring option
            # the recursion must stop right there. so return statement.

            if index >= len(candidates) or total > target:
                return

            # include the current element.
            current.append(candidates[index])
            total += candidates[index]
            dfs(index,current,total)

            total -= candidates[index]
            current.pop() # Backtrack to remove the current element
            
            # Not include the current element
            dfs(index + 1, current, total)
        


        dfs(0, [], 0)
        return result
# time complexity -- o(2^t where t is the target)
# because:
# if lets say i only was able to choose one number one time,
# then the height of recursion tree would be equal to N and that makes time complexity as 2^n.
# but here, i can make choose same number any no of times.
# so, lets say, 
# i have a array, [1] and my target is 7.
# so i could choose 1 7 times, [1,1,1,1,1,1,1] to get the result and this would create a tree of height of 7.
# so this soln has time complexity -- o(2^t where t is the target) 2 becasue there are two choices at each point, either to take it or not take it.
        