class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # # The idea is to sort the positon of the car, 
        # @ and caclaulate the time taken for car to reach the destination.
        # and we can find whether two cars would fleet(intersect or not) if car that was behind the first car has the time to reach the destination <= (smaller than or equal) to the front car.
        # so we come from the reverse side.
        # add distance to reach on stack. 
        # and lets say, we have two, distaces in stack, 
        # then we check, if the most recently add(top of stack) has smaller time or equal, if it is true, then they fleet, so we remove the second one.
        # and continue the process.

        pair = []

        for i in range(0, len(position)):
            pair.append([position[i], speed[i]])
        
        pair.sort()
        stack = []

        for i in range(len(pair) - 1 , -1 , -1 ):
            position = pair[i][0]
            speed = pair[i][1]
            
            time_taken_to_reach_destination = (target - position) / speed
            stack.append(time_taken_to_reach_destination)

            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

# Time complexity - o(nlogn) to sort the positions.

