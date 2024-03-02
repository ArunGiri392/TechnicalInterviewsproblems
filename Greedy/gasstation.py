class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        starting_point = 0

        for i in range(0, len(gas)):
            total += gas[i] - cost[i]
            # if my total gas needed ever becomes less than 0, meaning, we have less gas, than required. so we cannot move ahead from here.
            if total < 0:
                total = 0
                # we also , know, like if we cannot move forward from this point, so any points(station) between, this and starting point, will also not reach, so we should not calcualte them.
                starting_point = i + 1

        
        return starting_point


# Therefore, if we reach the end of the list and the total extra fuel is non-negative, it implies that we have enough fuel to complete the entire circular journey, including returning to the starting point